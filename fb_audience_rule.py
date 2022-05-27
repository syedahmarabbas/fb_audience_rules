from typing import Optional
from pydantic import BaseModel, HttpUrl, Field


class Filters(BaseModel):
    field: str
    operator: str
    value: str


class Filter(BaseModel):
    operator: str
    filters: list[Filters]
