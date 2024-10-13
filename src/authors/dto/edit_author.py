from pydantic import BaseModel, constr
from typing import Optional
from datetime import date


class EditAuthorDTO(BaseModel):
    nombre: constr(min_length=0, max_length=100)
    apellido: constr(min_length=0, max_length=100)
    fecha_nacimiento: Optional[date]
