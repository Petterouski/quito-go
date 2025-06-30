# Importa la clase FastAPI del paquete fastapi
from fastapi import FastAPI

# Importa el router del controlador de autenticación desde el módulo controllers
from controllers import auth_controller

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

# Incluye el router de autenticación en la aplicación principal
# Esto permite que las rutas definidas en auth_controller sean accesibles
app.include_router(auth_controller.router)
