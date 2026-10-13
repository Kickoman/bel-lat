"""The http_request line carries the client's User-Agent and the site it came from."""
import io
import json
import sys

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from service.logging_setup import LOGGED_TEXT, RequestLogMiddleware, setup_logging


@pytest.fixture
def lines(monkeypatch):
    """Capture stdout log lines. structlog writes to the sys.stdout it was configured with, so reconfigure."""
    buf = io.StringIO()
    monkeypatch.setattr(sys, "stdout", buf)
    setup_logging()
    yield lambda: [json.loads(line) for line in buf.getvalue().splitlines() if line.strip()]
    setup_logging()


@pytest.fixture
def client(lines):
    # A fresh app per test: the middleware binds its logger to the stdout of the moment it is built.
    app = FastAPI()

    @app.get("/translate/{style}")
    def translate(style: str):
        return {"style": style}

    app.add_middleware(RequestLogMiddleware)
    return TestClient(app)


def requests_logged(lines) -> list[dict]:
    return [event for event in lines() if event["stream"] == "http_request"]


def test_request_line_has_user_agent_and_foreign_referrer(client, lines):
    client.get("/translate/classic", headers={"user-agent": "Mozilla/5.0 (Linux)", "referer": "https://t.me/somechat"})
    [event] = requests_logged(lines)
    assert event["http_path"] == "/translate/{style}"
    assert event["user_agent"] == "Mozilla/5.0 (Linux)"
    assert event["referrer_host"] == "t.me"


def test_own_pages_and_broken_referrers_are_left_out(client, lines):
    client.get("/translate/classic", headers={"referer": "http://testserver/lacinka/"})
    client.get("/translate/classic", headers={"referer": "http://[::1"})
    client.get("/translate/classic")
    assert [("referrer_host" in event) for event in requests_logged(lines)] == [False, False, False]


def test_user_agent_is_cut(client, lines):
    client.get("/translate/classic", headers={"user-agent": "x" * 1000})
    [event] = requests_logged(lines)
    assert event["user_agent"] == "x" * LOGGED_TEXT
