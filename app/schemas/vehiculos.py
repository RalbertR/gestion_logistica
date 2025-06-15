from pydantic import BaseModel, ConfigDict

class VehiculoBase(BaseModel):
    tipo: str
    marca: str
    modelo: str
    anio: int
    patente: str
    en_servicio: bool = True
    
class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

