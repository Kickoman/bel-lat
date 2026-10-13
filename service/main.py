from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import bel_lat

from service.logging_setup import RequestLogMiddleware, get_logger, setup_logging

setup_logging()
log = get_logger(stream="internal")

app = FastAPI(
    title="bel-lat",
    version=bel_lat.__version__,
    description="Convert cyrillic Belarusian characters to Latin characters using transliteration.",
)
app.add_middleware(RequestLogMiddleware)


class Style(str, Enum):
    lacinka = "lacinka"
    geo_2000 = "geo-2000"
    geo_2023 = "geo-2023"


class TranslateRequest(BaseModel):
    text: str
    style: Style = Style.lacinka
    custom_replacements: list[tuple[str, list[str] | str]] = Field(default_factory=list)


class TranslateResponse(BaseModel):
    result: str


@app.get("/")
def info():
    return {"name": "bel-lat", "version": bel_lat.__version__, "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/translate", response_model=TranslateResponse)
def translate(request: TranslateRequest):
    try:
        result = bel_lat.translate(
            request.text,
            style=request.style.value,
            custom_replacements=request.custom_replacements,
        )
    except (TypeError, ValueError) as e:
        # Bad input, not a service fault -- warning, not error.
        log.warning(
            "translate_rejected",
            style=request.style.value,
            text=request.text,
            text_len=len(request.text),
            error=f"{type(e).__name__}: {e}",
        )
        raise HTTPException(status_code=400, detail=str(e))

    # NOTE: the submitted text and its result are logged in full, so whatever
    # users send lands in the log store and lives there for the stream's
    # retention period. Deliberate -- it makes transliteration bugs
    # reproducible from the logs alone.
    log.info(
        "translate",
        style=request.style.value,
        text=request.text,
        result=result,
        text_len=len(request.text),
        result_len=len(result),
        custom_replacements=len(request.custom_replacements),
    )
    return TranslateResponse(result=result)
