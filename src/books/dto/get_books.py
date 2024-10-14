from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
from uuid import UUID


class GetBooksDTO(BaseModel):
    id: Optional[str] = None
    author_id: Optional[str] = None
    titulo: Optional[str] = None
    fecha_publicacion: Optional[datetime] = None

    @validator("id")
    def validate_id(cls, value):
        if not value or not len(value):
            return value
        try:
            UUID(value)
            return value
        except ValueError:
            raise ValueError("El ID no es un UUID valido")

    @validator("author_id")
    def validate_author_id(cls, value):
        if not value or not len(value):
            return value
        try:
            UUID(value)
            return value
        except ValueError:
            raise ValueError("El ID no es un UUID valido")
