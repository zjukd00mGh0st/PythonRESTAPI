from pydantic import BaseModel
from typing import Optional
from datetime import date


class GetAuthorsDTO(BaseModel):
    id: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    fecha_creacion: Optional[date] = None

