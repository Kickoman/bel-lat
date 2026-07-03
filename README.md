# bel-lat

Convert cyrillic Belarusian characters to Latin characters using transliteration. Can transliterate in accordance with the ["Instruction on transliteration of geographical names"](https://en.wikipedia.org/wiki/Instruction_on_transliteration_of_Belarusian_geographical_names_with_letters_of_Latin_script) (2000 and 2023) or in accordance with the rules of the [Belarusian Latin alphabet (Łacinka)](https://en.wikipedia.org/wiki/Belarusian_Latin_alphabet).

This is a Python library plus a small HTTP API service exposing the same conversion. The project was originally an npm package (`@skip405/bel-lat`); see [CHANGELOG.md](CHANGELOG.md) for the rewrite notes.

## Library

### Installation

```
pip install -e .
```

### Usage

By default, the library transliterates in accordance with the Łacinka rules.

```python
from bel_lat import translate

translate('Лацінка')  # Łacinka
```

which is equivalent to:

```python
from bel_lat import translate

translate('Лацінка', style='lacinka')  # Łacinka
```

### Instruction for geographical names

You can specify conversion in accordance with the instructions for geographical names (2000 and 2023), e.g.

```python
from bel_lat import translate

translate('Шчучыншчына', style='geo-2000')  # Ščučynščyna
translate('Шчучыншчына', style='geo-2023')  # Shchuchynshchyna
```

### Basic replacements

The library allows you to specify your own replacement symbols.

```python
from bel_lat import translate

translate('№', custom_replacements=[('№', ['#'])])  # #
```

**N.B.** if you need more complex conversions please prepare the string beforehand using other means.

### Basic omissions

If you'd like to omit any characters from conversion you can specify `'_omitted'` as a value for a custom replacement.

```python
from bel_lat import translate

translate('абв', custom_replacements=[('б', '_omitted')])  # av
```

**N.B.** conversion is done on a per-character basis, it is not possible to omit multiple characters in a single call.

## API service

A small FastAPI service exposes the same conversion over HTTP.

### Running locally

```
pip install -e ".[service]"
uvicorn service.main:app --reload
```

### Endpoints

- `POST /translate` — convert text.
- `GET /health` — health check.
- `GET /` — basic service info.
- `GET /docs` — interactive Swagger UI (auto-generated).

### Examples

```shell
curl -X POST http://localhost:8000/translate \
  -H 'Content-Type: application/json' \
  -d '{"text": "прывітанне, сусвет"}'
# {"result":"pryvitannie, susviet"}

curl -X POST http://localhost:8000/translate \
  -H 'Content-Type: application/json' \
  -d '{"text": "Шчучыншчына", "style": "geo-2023"}'
# {"result":"Shchuchynshchyna"}

curl -X POST http://localhost:8000/translate \
  -H 'Content-Type: application/json' \
  -d '{"text": "№", "custom_replacements": [["№", ["#"]]]}'
# {"result":"#"}

curl http://localhost:8000/health
# {"status":"ok"}
```

## Docker

Build and run the API service in a container:

```
docker build -t bel-lat .
docker run --rm -p 8000:8000 bel-lat
```

Then the service is reachable at `http://localhost:8000` as described above.

### Running behind a reverse proxy on a sub-path

If the service isn't served from the domain root (e.g. `example.com/bel-lat` instead of `example.com`), set the `ROOT_PATH` environment variable to that prefix. This tells FastAPI to generate `/docs`, `/redoc` and `/openapi.json` links with the prefix included, so Swagger UI resolves correctly instead of requesting them from the domain root.

```shell
docker run --rm -p 8000:8000 -e ROOT_PATH=/bel-lat bel-lat
```

Matching nginx config (strips the prefix before proxying, same as the app expects with `ROOT_PATH` set):

```nginx
location /bel-lat/ {
        rewrite /bel-lat/(.*) /$1 break;
        proxy_pass      http://127.0.0.1:8000;
        proxy_redirect  off;
        proxy_set_header Host $host;
}
```

## Testing

```
pip install -e ".[dev,service]"
pytest
```

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
