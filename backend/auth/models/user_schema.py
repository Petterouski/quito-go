# Importamos las clases necesarias de pydantic para la validación de datos
from pydantic import BaseModel, EmailStr

# Clase que define el esquema de datos para el registro de un nuevo usuario
class UserRegister(BaseModel):
    """
    Modelo de datos para registrar un nuevo usuario.
    - email: Dirección de correo electrónico del usuario, validada automáticamente.
    - password: Contraseña del usuario, como cadena de texto.
    """
    email: EmailStr  # Validación automática para que sea un email válido
    password: str    # Contraseña del usuario

# Clase que define el esquema de datos para el inicio de sesión de un usuario
class UserLogin(BaseModel):
    """
    Modelo de datos para que un usuario inicie sesión.
    - email: Dirección de correo electrónico del usuario, validada automáticamente.
    - password: Contraseña del usuario, como cadena de texto.
    """
    email: EmailStr  # Validación automática para que sea un email válido
    password: str    # Contraseña del usuario
