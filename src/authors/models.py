from pydantic import BaseModel, validator
from datetime import date
from typing import Optional


class Author(BaseModel):
    id: Optional[str] = None
    nombre: str
    apellido: str
    fecha_nacimiento: date
    fecha_creacion: date

    @validator("nombre")
    def validate_name(cls, value):
        return value

    @validator("apellido")
    def validate_apellido(cls, value):
        return value

    
    @validator("fecha_nacimiento")
    def validate_fecha_nacimiento(cls, value):
        return value



# class Book(BaseModel):
#     id: Optional[str] = None
#     author_id: str
#     titulo: str
#     fecha_publicacion: datetime
#     fecha_creacion: datetime

#     @validator("titulo")
#     def validate_titulo(cls, value):
#         return value

#     @validator("fecha_publicacion")
#     def validate_titulo(cls, value):
#         return value

#     @validator("author_id")
#     def validate_titulo(cls, value):
#         return value