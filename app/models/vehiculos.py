from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, index=True)
    marca = Column(String)
    modelo = Column(String)
    anio = Column(Integer)
    patente = Column(String, unique=True, index=True)
    en_servicio = Column(Boolean, default=True)


    