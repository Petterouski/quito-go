from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from repositories.user_repository import UserRepository

SECRET_KEY = "quitogo_supersecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def register(self, email, password):
        if self.repo.find_by_email(email):
            raise HTTPException(status_code=400, detail="Email ya registrado")
        hashed_password = pwd_context.hash(password)
        self.repo.create_user(email, hashed_password)
        return {"message": "Usuario registrado"}

    def login(self, email, password):
        user = self.repo.find_by_email(email)
        if not user or not pwd_context.verify(password, user["password"]):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        access_token = self.create_access_token({"sub": user["email"]})
        return {"access_token": access_token, "token_type": "bearer"}

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

