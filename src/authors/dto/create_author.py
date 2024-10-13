from pydantic import BaseModel, constr
from datetime import date


class CreateAuthorDTO(BaseModel):
    nombre: constr(min_length=1, max_length=100)
    apellido: constr(min_length=1, max_length=100)
    fecha_nacimiento: date