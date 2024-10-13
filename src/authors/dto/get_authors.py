from pydantic import BaseModel
from typing import Optional
from datetime import date


class GetAuthorsDTO(BaseModel):
    id: Optional[str]
    nombre: Optional[str]
    apellido: Optional[str]
    fecha_nacimiento: Optional[date]
    fecha_creacion: Optional[date]
