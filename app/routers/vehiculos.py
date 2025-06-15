from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.schemas import vehiculos as schemas
from app.crud import vehiculos as crud
from app.database import get_db

router = APIRouter(prefix="/vehiculos", tags=["vehiculos"])

@router.post("/", response_model=schemas.VehiculoResponse)
async def crear_vehiculo(
    vehiculo: schemas.VehiculoCreate = Body(
        ...,
        example={
            "tipo": "Camioneta",
            "marca": "Toyota",
            "modelo": "Hilux",
            "anio": 2023,
            "patente": "ABC123",
            "en_servicio": True
        }
    ),
    db: Session = Depends(get_db)
):
    return crud.crear_vehiculo(db, vehiculo)

@router.get("/", response_model=list[schemas.VehiculoResponse])
def obtener_vehiculos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.obtener_vehiculos(db, skip, limit)

@router.get("/{vehiculo_id}", response_model=schemas.VehiculoResponse)
def obtener_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    db_vehiculo = crud.obtener_vehiculo(db, vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return db_vehiculo

@router.delete("/{vehiculo_id}", response_model=schemas.VehiculoResponse)
def eliminar_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = crud.eliminar_vehiculo(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehiculo no encontrado")
    return {"mensaje": "Vehiculo eliminado correctamente"}

