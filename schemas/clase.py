from pydantic import BaseModel, EmailStr
from typing import Optional

class Clase(BaseModel):
    id: Optional[int]
    nrc: str
    nombre: str
    academico: str    
    facultad: str 
    campus: str
    edificio: str
    aula: int   
    lunes: Optional[str]
    martes: Optional[str]
    miercoles: Optional[str]
    jueves: Optional[str]
    viernes: Optional[str]
    sabado: Optional[str]