from fastapi import FastAPI
from app.routers import vehiculos

app = FastAPI(title="Sistema de Gestion Logistica")
app.include_router(vehiculos.router)
@app.get("/")
def root():
    return {"message": "Sistema en funcionamiento",
            "modulos": ["Automotores", "Armamento", "Comunicaciones", "Inspeccion y Deteccion"]}




