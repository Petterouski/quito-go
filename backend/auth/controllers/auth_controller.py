from fastapi import APIRouter, Depends
from auth.models.user_schema import UserRegister, UserLogin
from auth.config.db_config import get_mysql_session
from auth.services.auth_service import AuthService

# Crear un enrutador de FastAPI con prefijo "/auth" y etiqueta "Auth" para la documentación
router = APIRouter(prefix="/auth", tags=["Auth"])

def get_auth_service() -> AuthService:
    """
    Dependencia que crea una instancia de AuthService, proporcionando la sesión de base de datos.

    Retorna:
        AuthService: Una instancia del servicio de autenticación con conexión a la base de datos.
    """
    # Obtiene una sesión de base de datos MySQL usando la función de configuración
    db = get_mysql_session()
    # Devuelve una instancia del servicio de autenticación, pasando la sesión de la base de datos
    return AuthService(db)

@router.post("/register")
def register(user: UserRegister, service: AuthService = Depends(get_auth_service)):
    """
    Endpoint para registrar un nuevo usuario.

    Args:
        user (UserRegister): Objeto que contiene el email y la contraseña del usuario a registrar.
        service (AuthService): Instancia del servicio de autenticación, inyectada automáticamente.

    Retorna:
        dict: Resultado del proceso de registro, típicamente incluyendo tokens o estado.
    """
    # Llama al método register del servicio de autenticación con los datos del usuario
    return service.register(user.email, user.password)

@router.post("/login")
def login(user: UserLogin, service: AuthService = Depends(get_auth_service)):
    """
    Endpoint para iniciar sesión de un usuario existente.

    Args:
        user (UserLogin): Objeto que contiene el email y la contraseña del usuario.
        service (AuthService): Instancia del servicio de autenticación, inyectada automáticamente.

    Retorna:
        dict: Resultado del proceso de login, como tokens de sesión o mensajes de error.
    """
    # Llama al método login del servicio de autenticación con los datos del usuario
    return service.login(user.email, user.password)
