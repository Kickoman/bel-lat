from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

import bel_lat

app = FastAPI(
    title="bel-lat",
    version=bel_lat.__version__,
    description="Convert cyrillic Belarusian characters to Latin characters using transliteration.",
)


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
        raise HTTPException(status_code=400, detail=str(e))

    return TranslateResponse(result=result)
