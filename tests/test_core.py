import pytest

from bel_lat import translate


def test_smoke():
    assert translate("прывітанне, сусвет") == "pryvitannie, susviet"

    assert translate("Шчучыншчына", style="lacinka") == "Ščučynščyna"
    assert translate("Шчучыншчына", style="geo-2000") == "Ščučynščyna"
    assert translate("Шчучыншчына", style="geo-2023") == "Shchuchynshchyna"


class TestLetters:
    def test_lowercase(self):
        assert translate("а") == "a"
        assert translate("б") == "b"
        assert translate("в") == "v"
        assert translate("г") == "h"
        assert translate("ґ") == "g"
        assert translate("д") == "d"
        assert translate("ж") == "ž"
        assert translate("і") == "i"
        assert translate("й") == "j"
        assert translate("к") == "k"
        assert translate("м") == "m"
        assert translate("о") == "o"
        assert translate("п") == "p"
        assert translate("р") == "r"
        assert translate("т") == "t"
        assert translate("у") == "u"
        assert translate("ў") == "ŭ"
        assert translate("ф") == "f"
        assert translate("х") == "ch"
        assert translate("ч") == "č"
        assert translate("ш") == "š"
        assert translate("ы") == "y"
        assert translate("э") == "e"

    def test_uppercase(self):
        assert translate("А") == "A"
        assert translate("Б") == "B"
        assert translate("В") == "V"
        assert translate("Г") == "H"
        assert translate("Ґ") == "G"
        assert translate("Д") == "D"
        assert translate("Ж") == "Ž"
        assert translate("І") == "I"
        assert translate("Й") == "J"
        assert translate("К") == "K"
        assert translate("М") == "M"
        assert translate("О") == "O"
        assert translate("П") == "P"
        assert translate("Р") == "R"
        assert translate("Т") == "T"
        assert translate("У") == "U"
        assert translate("Ў") == "Ŭ"
        assert translate("Ф") == "F"
        assert translate("Х") == "Ch"
        assert translate("Ч") == "Č"
        assert translate("Ш") == "Š"
        assert translate("Ы") == "Y"
        assert translate("Э") == "E"

    def test_omissions(self):
        assert translate("ь") == ""
        assert translate("’") == ""
        assert translate("‘") == ""


class TestGeo2023:
    def test_lowercase(self):
        assert translate("г", style="geo-2023") == "g"
        assert translate("ж", style="geo-2023") == "zh"
        assert translate("ў", style="geo-2023") == "w"
        assert translate("х", style="geo-2023") == "h"
        assert translate("ч", style="geo-2023") == "ch"
        assert translate("ш", style="geo-2023") == "sh"

    def test_uppercase(self):
        assert translate("Г", style="geo-2023") == "G"
        assert translate("Ж", style="geo-2023") == "Zh"
        assert translate("Ў", style="geo-2023") == "W"
        assert translate("Х", style="geo-2023") == "H"
        assert translate("Ч", style="geo-2023") == "Ch"
        assert translate("Ш", style="geo-2023") == "Sh"

    def test_capslock(self):
        assert translate("ГА", style="geo-2023") == "GA"
        assert translate("ЖБ", style="geo-2023") == "ZHB"
        assert translate("ЎВ", style="geo-2023") == "WV"
        assert translate("ХА", style="geo-2023") == "HA"
        assert translate("ЧА", style="geo-2023") == "CHA"
        assert translate("ША", style="geo-2023") == "SHA"


class TestEJoJuJaRenderWithJ:
    def test_start_of_word_lowercase(self):
        assert translate("е") == "je"
        assert translate("ё") == "jo"
        assert translate("ю") == "ju"
        assert translate("я") == "ja"

    def test_start_of_word_uppercase(self):
        assert translate("Е") == "Je"
        assert translate("Ё") == "Jo"
        assert translate("Ю") == "Ju"
        assert translate("Я") == "Ja"

    def test_start_of_word_capslock(self):
        assert translate("ЕА") == "JEA"
        assert translate("ЁВ") == "JOV"
        assert translate("ЮБ") == "JUB"
        assert translate("ЯГ") == "JAH"

    def test_after_vowels_lowercase(self):
        assert translate("ае") == "aje"
        assert translate("іе") == "ije"
        assert translate("ое") == "oje"
        assert translate("уе") == "uje"
        assert translate("ые") == "yje"
        assert translate("эе") == "eje"

        assert translate("аё") == "ajo"
        assert translate("іё") == "ijo"
        assert translate("оё") == "ojo"
        assert translate("уё") == "ujo"
        assert translate("ыё") == "yjo"
        assert translate("эё") == "ejo"

        assert translate("аю") == "aju"
        assert translate("ію") == "iju"
        assert translate("ою") == "oju"
        assert translate("ую") == "uju"
        assert translate("ыю") == "yju"
        assert translate("эю") == "eju"

        assert translate("ая") == "aja"
        assert translate("ія") == "ija"
        assert translate("оя") == "oja"
        assert translate("уя") == "uja"
        assert translate("ыя") == "yja"
        assert translate("эя") == "eja"

    def test_after_vowels_uppercase(self):
        assert translate("аЕ") == "aJe"
        assert translate("іЕ") == "iJe"
        assert translate("оЕ") == "oJe"
        assert translate("уЕ") == "uJe"
        assert translate("ыЕ") == "yJe"
        assert translate("эЕ") == "eJe"

        assert translate("аЁ") == "aJo"
        assert translate("іЁ") == "iJo"
        assert translate("оЁ") == "oJo"
        assert translate("уЁ") == "uJo"
        assert translate("ыЁ") == "yJo"
        assert translate("эЁ") == "eJo"

        assert translate("аЮ") == "aJu"
        assert translate("іЮ") == "iJu"
        assert translate("оЮ") == "oJu"
        assert translate("уЮ") == "uJu"
        assert translate("ыЮ") == "yJu"
        assert translate("эЮ") == "eJu"

        assert translate("аЯ") == "aJa"
        assert translate("іЯ") == "iJa"
        assert translate("оЯ") == "oJa"
        assert translate("уЯ") == "uJa"
        assert translate("ыЯ") == "yJa"
        assert translate("эЯ") == "eJa"

    def test_after_vowels_capslock(self):
        assert translate("аЕА") == "aJEA"
        assert translate("іЕБ") == "iJEB"
        assert translate("оЕВ") == "oJEV"
        assert translate("уЕГ") == "uJEH"
        assert translate("ыЕД") == "yJED"
        assert translate("эЕІ") == "eJEI"

        assert translate("аЁА") == "aJOA"
        assert translate("іЁБ") == "iJOB"
        assert translate("оЁВ") == "oJOV"
        assert translate("уЁГ") == "uJOH"
        assert translate("ыЁД") == "yJOD"
        assert translate("эЁІ") == "eJOI"

        assert translate("аЮА") == "aJUA"
        assert translate("іЮБ") == "iJUB"
        assert translate("оЮВ") == "oJUV"
        assert translate("уЮГ") == "uJUH"
        assert translate("ыЮД") == "yJUD"
        assert translate("эЮІ") == "eJUI"

        assert translate("аЯА") == "aJAA"
        assert translate("іЯБ") == "iJAB"
        assert translate("оЯВ") == "oJAV"
        assert translate("уЯГ") == "uJAH"
        assert translate("ыЯД") == "yJAD"
        assert translate("эЯІ") == "eJAI"

    def test_after_apostrophe_lowercase(self):
        assert translate("’е") == "je"
        assert translate("‘е") == "je"

        assert translate("’ё") == "jo"
        assert translate("‘ё") == "jo"

        assert translate("’ю") == "ju"
        assert translate("‘ю") == "ju"

        assert translate("’я") == "ja"
        assert translate("‘я") == "ja"

    def test_after_apostrophe_uppercase(self):
        assert translate("’Е") == "Je"
        assert translate("‘Е") == "Je"

        assert translate("’Ё") == "Jo"
        assert translate("‘Ё") == "Jo"

        assert translate("’Ю") == "Ju"
        assert translate("‘Ю") == "Ju"

        assert translate("’Я") == "Ja"
        assert translate("‘Я") == "Ja"

    def test_after_apostrophe_capslock(self):
        assert translate("’ЕА") == "JEA"
        assert translate("‘ЕА") == "JEA"

        assert translate("’ЁА") == "JOA"
        assert translate("‘ЁА") == "JOA"

        assert translate("’ЮА") == "JUA"
        assert translate("‘ЮА") == "JUA"

        assert translate("’ЯА") == "JAA"
        assert translate("‘ЯА") == "JAA"

    def test_after_u_and_soft_sign_lowercase(self):
        assert translate("ўе") == "ŭje"
        assert translate("ўё") == "ŭjo"
        assert translate("ўю") == "ŭju"
        assert translate("ўя") == "ŭja"

        assert translate("ье") == "je"
        assert translate("ьё") == "jo"
        assert translate("ью") == "ju"
        assert translate("ья") == "ja"

    def test_after_u_and_soft_sign_uppercase(self):
        assert translate("ўЕ") == "ŭJe"
        assert translate("ўЁ") == "ŭJo"
        assert translate("ўЮ") == "ŭJu"
        assert translate("ўЯ") == "ŭJa"

        assert translate("ьЕ") == "Je"
        assert translate("ьЁ") == "Jo"
        assert translate("ьЮ") == "Ju"
        assert translate("ьЯ") == "Ja"

    def test_after_u_and_soft_sign_capslock(self):
        assert translate("ўЕА") == "ŭJEA"
        assert translate("ўЁА") == "ŭJOA"
        assert translate("ўЮА") == "ŭJUA"
        assert translate("ўЯА") == "ŭJAA"

        assert translate("ьЕА") == "JEA"
        assert translate("ьЁА") == "JOA"
        assert translate("ьЮА") == "JUA"
        assert translate("ьЯА") == "JAA"


class TestEJoJuJaRenderWithIAfterConsonants:
    def test_lowercase(self):
        assert translate("бе") == "bie"
        assert translate("бё") == "bio"
        assert translate("бю") == "biu"
        assert translate("бя") == "bia"

    def test_uppercase(self):
        assert translate("бЕ") == "bIe"
        assert translate("бЁ") == "bIo"
        assert translate("бЮ") == "bIu"
        assert translate("бЯ") == "bIa"

    def test_capslock(self):
        assert translate("бЕА") == "bIEA"
        assert translate("бЁВ") == "bIOV"
        assert translate("бЮБ") == "bIUB"
        assert translate("бЯВ") == "bIAV"


def test_h_renders_as_ch_on_capslock():
    assert translate("ХА") == "CHA"


class TestZNSC:
    def test_render_without_acute_accent(self):
        assert translate("з") == "z"
        assert translate("н") == "n"
        assert translate("с") == "s"
        assert translate("ц") == "c"

        assert translate("З") == "Z"
        assert translate("Н") == "N"
        assert translate("С") == "S"
        assert translate("Ц") == "C"

    def test_render_with_acute_accent_before_soft_sign(self):
        assert translate("зь") == "ź"
        assert translate("нь") == "ń"
        assert translate("сь") == "ś"
        assert translate("ць") == "ć"

        assert translate("Зь") == "Ź"
        assert translate("Нь") == "Ń"
        assert translate("Сь") == "Ś"
        assert translate("Ць") == "Ć"

    def test_geo_2023(self):
        assert translate("з", style="geo-2023") == "z"
        assert translate("н", style="geo-2023") == "n"
        assert translate("с", style="geo-2023") == "s"
        assert translate("ц", style="geo-2023") == "c"

        assert translate("З", style="geo-2023") == "Z"
        assert translate("Н", style="geo-2023") == "N"
        assert translate("С", style="geo-2023") == "S"
        assert translate("Ц", style="geo-2023") == "C"


class TestL:
    def test_geo_2000_without_acute_sign(self):
        assert translate("л", style="geo-2000") == "l"
        assert translate("Л", style="geo-2000") == "L"

    def test_geo_2000_with_acute_sign_before_soft_sign(self):
        assert translate("ль", style="geo-2000") == "ĺ"
        assert translate("Ль", style="geo-2000") == "Ĺ"

    def test_geo_2023_renders_as_l(self):
        assert translate("л", style="geo-2023") == "l"
        assert translate("Л", style="geo-2023") == "L"

    def test_lacinka_renders_with_dash_sign(self):
        assert translate("л", style="lacinka") == "ł"
        assert translate("Л", style="lacinka") == "Ł"

    def test_lacinka_no_dash_before_e_jo_ju_i_l_ja_soft_sign(self):
        assert translate("ле", style="lacinka") == "le"
        assert translate("лё", style="lacinka") == "lo"
        assert translate("лю", style="lacinka") == "lu"
        assert translate("ля", style="lacinka") == "la"
        assert translate("ль", style="lacinka") == "l"
        assert translate("лі", style="lacinka") == "li"
        assert translate("лле", style="lacinka") == "lle"

        assert translate("Ле", style="lacinka") == "Le"
        assert translate("Лё", style="lacinka") == "Lo"
        assert translate("Лю", style="lacinka") == "Lu"
        assert translate("Ля", style="lacinka") == "La"
        assert translate("Ль", style="lacinka") == "L"
        assert translate("Лі", style="lacinka") == "Li"
        assert translate("Лле", style="lacinka") == "Lle"


class TestMisc:
    def test_throws_type_error_on_wrong_data_type(self):
        with pytest.raises(TypeError):
            translate(1)

    def test_ignores_unknown_characters(self):
        assert translate("xyz") == "xyz"

    def test_does_not_parse_empty_strings(self):
        assert translate("") == ""

    def test_allows_basic_custom_replacements(self):
        assert translate("№", custom_replacements=[("№", ["#"])]) == "#"

    def test_allows_basic_custom_removals(self):
        assert translate("абв", custom_replacements=[("б", "_omitted")]) == "av"
