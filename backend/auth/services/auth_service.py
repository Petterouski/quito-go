# Importación de las librerías necesarias
from passlib.context import CryptContext  # Para manejo de hashing de contraseñas
from jose import jwt  # Para generación y validación de tokens JWT
from datetime import datetime, timedelta  # Para manejo de fechas y tiempos
from fastapi import HTTPException  # Para lanzar excepciones HTTP en FastAPI
from repositories.user_repository import UserRepository  # Repositorio para gestión de usuarios en la base de datos

# Configuración de secretos y parámetros para los tokens JWT
SECRET_KEY = "quitogo_supersecret"  # Clave secreta para firmar los tokens (debe mantenerse segura en producción)
ALGORITHM = "HS256"  # Algoritmo de encriptación para JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Tiempo de expiración del token en minutos

# Configuración del contexto de hashing para contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, db):
        # Inicializa el servicio con un repositorio de usuario
        self.repo = UserRepository(db)

    def register(self, email, password):
        """
        Registra un nuevo usuario en el sistema.
        - Verifica si el email ya está registrado.
        - Hashea la contraseña.
        - Crea y guarda el usuario en la base de datos.
        """
        # Comprobar si el email ya existe en la base de datos
        if self.repo.find_by_email(email):
            # Lanzar error si el email ya está registrado
            raise HTTPException(status_code=400, detail="Email ya registrado")
        
        # Hashear la contraseña proporcionada
        hashed_password = pwd_context.hash(password)
        
        # Crear y guardar el nuevo usuario con el email y la contraseña hasheada
        self.repo.create_user(email, hashed_password)
        
        # Retornar confirmación de registro
        return {"message": "Usuario registrado"}

    def login(self, email, password):
        """
        Autentica un usuario y genera un token JWT válido.
        - Verifica si el usuario existe.
        - Verifica si la contraseña es correcta.
        - Genera y devuelve un token de acceso.
        """
        # Buscar usuario por email
        user = self.repo.find_by_email(email)
        # Verificar existencia del usuario y validez de la contraseña
        if not user or not pwd_context.verify(password, user["password"]):
            # Lanzar error si las credenciales no son válidas
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        
        # Crear un token de acceso con la información del usuario
        access_token = self.create_access_token({"sub": user["email"]})
        
        # Devolver el token y el tipo de token
        return {"access_token": access_token, "token_type": "bearer"}

    def create_access_token(self, data: dict):
        """
        Genera un token JWT con un tiempo de expiración definido.
        - Añade la fecha de expiración a los datos.
        - Firma el token con la clave secreta y el algoritmo especificado.
        """
        # Copiar los datos para no modificar el original
        to_encode = data.copy()
        # Calcular la fecha y hora de expiración
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # Añadir la fecha de expiración a los datos del token
        to_encode.update({"exp": expire})
        # Codificar el token JWT
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        # Devolver el token codificado
        return encoded_jwt
    