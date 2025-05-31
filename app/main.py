from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Sistema de Gestion Logistica")

@app.get("/")
def root():
    return {"message": "Sistema en funcionamiento",
            "modulos": ["Automotores", "Armamento", "Comunicaciones", "Inspeccion y Deteccion"]}


