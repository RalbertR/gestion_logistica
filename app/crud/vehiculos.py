from sqlalchemy.orm import Session
from app.models.vehiculos import Vehiculo
from app.schemas.vehiculos import VehiculoCreate

def crear_vehiculo(db: Session, vehiculo: VehiculoCreate):
    db_vehiculo = Vehiculo(**vehiculo.model_dump())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def obtener_vehiculos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vehiculo).offset(skip).limit(limit).all()

def obtener_vehiculo(db: Session, vehiculo_id: int):
    return db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()

def eliminar_vehiculo(db: Session, vehiculo_id: int):
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if vehiculo:
        db.delete(vehiculo)
        db.commit()
    return vehiculo

