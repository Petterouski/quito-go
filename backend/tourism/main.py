from fastapi import FastAPI
from app.controllers import package_controller, reservation_controller
from app.controllers import auth_controller  # si ya lo moviste aquí

from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Rutas
app.include_router(package_controller.router)
app.include_router(reservation_controller.router)
app.include_router(auth_controller.router)  # Registro y login

# Frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
