from fastapi.testclient import TestClient

from service.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_translate_default_style():
    response = client.post("/translate", json={"text": "прывітанне, сусвет"})
    assert response.status_code == 200
    assert response.json() == {"result": "pryvitannie, susviet"}


def test_translate_geo_2023_style():
    response = client.post(
        "/translate", json={"text": "Шчучыншчына", "style": "geo-2023"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": "Shchuchynshchyna"}


def test_translate_custom_replacements():
    response = client.post(
        "/translate",
        json={"text": "№", "custom_replacements": [["№", ["#"]]]},
    )
    assert response.status_code == 200
    assert response.json() == {"result": "#"}


def test_translate_invalid_style_returns_422():
    response = client.post(
        "/translate", json={"text": "прывітанне", "style": "invalid-style"}
    )
    assert response.status_code == 422
