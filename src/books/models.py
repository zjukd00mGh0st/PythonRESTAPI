from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime


class Book(BaseModel):
    id: Optional[str] = None
    author_id: str
    titulo: str
    fecha_publicacion: datetime
    fecha_creacion: datetime

    @validator("titulo")
    def validate_titulo(cls, value):
        return value

    @validator("fecha_publicacion")
    def validate_titulo(cls, value):
        return value

    @validator("author_id")
    def validate_titulo(cls, value):
        return value
