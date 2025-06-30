from fastapi import APIRouter, Depends
from domain.dto.package_dto import PackageDTO
from config.db_config import get_mysql_session
from infrastructure.factories.mysql_factory import MySQLFactory
from application.services.package_service import PackageService
from auth.utils.jwt_bearer import JWTBearer  # ← Importar validador

router = APIRouter()

@router.post("/packages", dependencies=[Depends(JWTBearer())])
def create_package(data: PackageDTO, db=Depends(get_mysql_session)):
    service = PackageService(MySQLFactory(db))
    service.create_package(data)
    return {"message": "Package created"}

@router.get("/packages")
def list_packages(db=Depends(get_mysql_session)):
    service = PackageService(MySQLFactory(db))
    return service.list_packages()

@router.put("/packages/{package_id}", dependencies=[Depends(JWTBearer())])
def update_package(package_id: int, data: PackageDTO, db=Depends(get_mysql_session)):
    service = PackageService(MySQLFactory(db))
    return service.update_package(package_id, data)

@router.delete("/packages/{package_id}", dependencies=[Depends(JWTBearer())])
def delete_package(package_id: int, db=Depends(get_mysql_session)):
    service = PackageService(MySQLFactory(db))
    return service.delete_package(package_id)
