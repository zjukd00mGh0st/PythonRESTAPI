from pydantic import BaseModel, constr, validator
from typing import Optional
from datetime import date
from uuid import UUID


class EditAuthorDTO(BaseModel):
    id: str
    nombre: constr(min_length=0, max_length=100)
    apellido: constr(min_length=0, max_length=100)
    fecha_nacimiento: Optional[date]

    @validator("id")
    def validate_id(cls, value):
        try:
            UUID(value)
            return value
        except ValueError:
            raise ValueError("El ID no es un UUID valido")
