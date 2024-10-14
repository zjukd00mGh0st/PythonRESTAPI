from pydantic import BaseModel, validator, constr
from datetime import datetime, timezone
from uuid import UUID


class CreateBookDTO(BaseModel):
    author_id: str
    titulo: constr(min_length=1, max_length=100)
    fecha_publicacion: datetime

    @validator("author_id")
    def validate_author_id(cls, value):
        try:
           UUID(value)
           return value
        except ValueError as e:
            raise ValueError("El ID no es un UUID valido")

    @validator("fecha_publicacion")
    def validate_fecha_publicacion(cls, value):
        current_time = datetime.now(timezone.utc)
        value = value.replace(tzinfo=timezone.utc)
        if value > current_time:
            raise ValueError("La fecha de publicacion no puede ser en el futuro")
        return value
