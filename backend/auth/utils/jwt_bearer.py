from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

# Clave secreta utilizada para firmar y verificar los tokens JWT.
SECRET_KEY = "quitogo_supersecret"
# Algoritmo de encriptación utilizado para firmar los tokens JWT.
ALGORITHM = "HS256"

# Clase personalizada que extiende HTTPBearer para agregar lógica de validación de JWT
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        """
        Inicializa la instancia de la clase JWTBearer, heredando de HTTPBearer.
        
        Args:
            auto_error (bool): Si es True, lanzará un error automáticamente cuando
                               las credenciales no estén presentes o sean inválidas.
        """
        # Llamada al constructor de la clase base con el parámetro auto_error
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        Método asíncrono que procesa la solicitud para extraer y validar el token JWT.
        
        Args:
            request (Request): La solicitud HTTP entrante.
        
        Retorna:
            dict: El payload decodificado del token JWT si la validación es exitosa.
        
        Lanza:
            HTTPException: Si el token no se proporciona o es inválido/expirado.
        """
        # Intenta obtener las credenciales de autorización de la cabecera
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        
        if credentials:
            try:
                # Decodifica el token JWT usando la clave secreta y el algoritmo definido
                payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
                # Retorna el payload decodificado si la decodificación es exitosa
                return payload
            except JWTError:
                # Lanza una excepción si el token es inválido o ha expirado
                raise HTTPException(status_code=403, detail="Token inválido o expirado")
        # Si no se proporcionan credenciales, lanza una excepción
        raise HTTPException(status_code=403, detail="Token no proporcionado")
