_BASE_REPLACEMENTS = (
    ("а", ["a"]),
    ("б", ["b"]),
    ("в", ["v"]),
    ("г", ["h", "g"]),
    ("ґ", ["g"]),
    ("д", ["d"]),
    ("е", ["ie", "je", "e"]),
    ("ё", ["io", "jo", "o"]),
    ("ж", ["z", "ž", "zh"]),
    ("з", ["z", "ź"]),
    ("і", ["i"]),
    ("й", ["j"]),
    ("к", ["k"]),
    ("л", ["l", "ł", "ĺ"]),
    ("м", ["m"]),
    ("н", ["n", "ń"]),
    ("о", ["o"]),
    ("п", ["p"]),
    ("р", ["r"]),
    ("с", ["s", "ś"]),
    ("т", ["t"]),
    ("у", ["u"]),
    ("ў", ["u", "ŭ", "w"]),
    ("ф", ["f"]),
    ("х", ["ch", "h"]),
    ("ц", ["c", "ć"]),
    ("ч", ["c", "č", "ch"]),
    ("ш", ["s", "š", "sh"]),
    ("ь", "_omitted"),
    ("ы", ["y"]),
    ("э", ["e"]),
    ("ю", ["iu", "ju", "u"]),
    ("я", ["ia", "ja", "a"]),
    ("’", "_omitted"),
    ("‘", "_omitted"),
)

_SPECIAL_CASES = {"е", "ё", "ж", "з", "л", "н", "с", "ў", "ц", "ч", "ш", "ю", "я"}


def _process_return_value(value, char, next_char, style):
    if char == char.upper() and char != char.lower():
        if next_char != "" and next_char == next_char.upper():
            return value.upper()

        return value[0].upper() + value[1:]

    return value


def _process_special_case(char, next_char, prev_char, style, replacement):
    index = 0
    lower = char.lower()
    next_lower = next_char.lower()
    prev_lower = prev_char.lower()

    if lower == "ў":
        index = 1

        if style == "geo-2023":
            index = 2
    elif lower == "л":
        if style == "geo-2000":
            if next_lower in ("ь",):
                index = 2
            else:
                index = 0
        elif style == "lacinka":
            if next_lower in ("е", "ё", "і", "л", "ю", "я", "ь"):
                index = 0
            else:
                index = 1
    elif lower in ("е", "ё", "ю", "я"):
        if prev_lower in ("а", "і", "о", "у", "ы", "ў", "э", "ь", "’", "‘") or prev_char == "":
            index = 1
        elif prev_lower == "л" and style == "lacinka":
            index = 2
    elif lower in ("з", "н", "с", "ц"):
        if next_lower == "ь":
            index = 1
        if style == "geo-2023":
            index = 0
    elif lower in ("ж", "ч", "ш"):
        index = 1

        if style == "geo-2023":
            index = 2

    return _process_return_value(replacement[index], char, next_char, style)


def _process_char(char, next_char, prev_char, style, replacement):
    if replacement == "_omitted":
        return ""

    if char.lower() in _SPECIAL_CASES:
        return _process_special_case(char, next_char, prev_char, style, replacement)

    replacement_value = replacement[0]

    if style == "geo-2023" and len(replacement) > 1 and replacement[1]:
        replacement_value = replacement[1]

    return _process_return_value(replacement_value, char, next_char, style)


def translate(text, style="lacinka", custom_replacements=None):
    if not isinstance(text, str):
        raise TypeError("Needs a string")

    custom_replacements = custom_replacements or []

    replacements = dict(_BASE_REPLACEMENTS)
    replacements.update(custom_replacements)

    words = []

    for word in text.split(" "):
        if word == "":
            words.append("")
            continue

        result_for_word = []

        for i, char in enumerate(word):
            replacement = replacements.get(char.lower())

            if not replacement:
                result_for_word.append(char)
                continue

            next_char = word[i + 1] if i + 1 < len(word) else ""
            prev_char = word[i - 1] if i > 0 else ""

            result_for_word.append(_process_char(char, next_char, prev_char, style, replacement))

        words.append("".join(result_for_word))

    return " ".join(words)
