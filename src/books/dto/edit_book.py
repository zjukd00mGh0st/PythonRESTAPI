from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
from uuid import UUID


class EditBookDTO(BaseModel):
    id: str
    titulo: Optional[str]
    fecha_publicacion: Optional[datetime]

    @validator("id")
    def validate_id(cls, value):
        try:
            UUID(value)
            return value
        except ValueError:
            raise ValueError("El ID no es un UUID valido")
