from pydantic import BaseModel, ValidationError, validator
import uuid


class GetEntityByIDDTO(BaseModel):
    id: str

    @validator("id")
    def validate_id(cls, value):
        try:
            uuid.UUID(value)
            return value
        except ValueError as e:
            print(str(e))
            raise ValueError("Invalid UUUID value")