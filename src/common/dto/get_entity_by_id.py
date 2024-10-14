from pydantic import BaseModel, ValidationError, validator
from uuid import UUID


class GetEntityByIDDTO(BaseModel):
    id: str

    @validator("id")
    def validate_id(cls, value):
        try:
            UUID(value)
            return value
        except ValueError:
            raise ValueError("El ID no es un UUID valido")