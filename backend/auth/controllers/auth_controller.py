from fastapi import APIRouter, Depends
from auth.models.user_schema import UserRegister, UserLogin
from auth.config.db_config import get_mysql_session
from auth.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_auth_service():
    db = get_mysql_session()
    return AuthService(db)

@router.post("/register")
def register(user: UserRegister, service: AuthService = Depends(get_auth_service)):
    return service.register(user.email, user.password)

@router.post("/login")
def login(user: UserLogin, service: AuthService = Depends(get_auth_service)):
    return service.login(user.email, user.password)
