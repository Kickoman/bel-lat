# Changelog

## Unreleased

### Changed

- The ASCII apostrophe `'` and the modifier letter apostrophe `ʼ` are omitted like `’` and `‘`, and `е`, `ё`, `ю`, `я` after them render with `j` (`сям'я` → `siamja`).

### Fixed

- `е`, `ё`, `ю`, `я` after punctuation and other non-letters render with `j` as at the start of a word (`/ёсьць` → `/jość`).
- Multi-letter replacements keep upper case at the end of an ALL-CAPS word and before punctuation, hyphens and stress marks (`ЖЫВЕ!` → `ŽYVIE!`, `МЕ́СЦА` → `MIÉSCA`).
- A capital letter followed by punctuation or a stress mark is no longer treated as ALL-CAPS (`Я, як і ты` → `Ja, jak i ty`).
- A lone capital letter takes its case from the neighbouring words (`Я ІДУ` → `JA IDU`, `Я іду` → `Ja idu`).
- Custom replacements with a single value for `е`, `ё`, `ю`, `я` and other context-dependent letters no longer raise `IndexError`.

## v3.0.0 - 2026-07-02

### Changed

- **Breaking:** Rewritten from JavaScript (npm `@skip405/bel-lat`) to Python. Package renamed to `bel-lat` (PyPI), importable as `bel_lat`.
- **Breaking:** API is now `translate(text, style="lacinka", custom_replacements=None)` (snake_case, keyword args) instead of `belLat(string, { style, customReplacements })`.

### Added

- FastAPI-based HTTP service (`service/`) exposing `POST /translate`, `GET /health`, and auto-generated docs at `/docs`.
- `Dockerfile` for building and running the service in a container.

### Removed

- **Breaking:** npm package, `index.js`, the Jest test suite, and `package.json`.

## v2.0.1 - 2023-05-04

### Changed

- Conversion of `л` and `е`, `ё`, `ю`, `я` after it for lacinka style

## v2.0.0 - 2023-04-05

### Changed

- **Breaking:** `geographical` option changed into `geo-2000`
- Bump `jest` to v29.5.0
- Internal data structure

### Added

- `geo-2023` style option

### Removed

- **Breaking:** `slugify` style option and @sindresorhus/slugify dependency
- **Breaking:** `geographical` style option. Use `geo-2000` instead

## v1.0.0 - 2022-12-30

Initial version.