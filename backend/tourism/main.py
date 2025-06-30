from fastapi import FastAPI
from app.controllers import package_controller, reservation_controller
from app.controllers import auth_controller  # Importa el controlador de autenticación (registro y login)
from fastapi.staticfiles import StaticFiles  # Para servir archivos estáticos del frontend

# Crear instancia de la aplicación FastAPI
app = FastAPI()

# Incluir las rutas definidas en los controladores
app.include_router(package_controller.router)  # Rutas relacionadas con paquetes
app.include_router(reservation_controller.router)  # Rutas relacionadas con reservaciones
app.include_router(auth_controller.router)  # Rutas para autenticación (registro y login)

# Servir la interfaz frontend desde la carpeta 'frontend'
# Esto hace que la interfaz esté accesible en la raíz del servidor
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
