# Importaciones necesarias desde las librerías y módulos internos
from fastapi import APIRouter, Depends
from domain.dto.package_dto import PackageDTO  # DTO para transferencia de datos de paquetes
from config.db_config import get_mysql_session  # Función para obtener la sesión de base de datos MySQL
from infrastructure.factories.mysql_factory import MySQLFactory  # Fábrica para crear instancias de acceso a MySQL
from application.services.package_service import PackageService  # Servicio de negocio para gestión de paquetes
from auth.utils.jwt_bearer import JWTBearer  # Validador JWT para autenticación basada en Bearer tokens

# Crear un enrutador para agrupar las rutas relacionadas con paquetes
router = APIRouter()

# Endpoint para crear un nuevo paquete
@router.post(
    "/packages",  # Ruta del endpoint
    dependencies=[Depends(JWTBearer())]  # Requiere autenticación JWT
)
def create_package(
    data: PackageDTO,  # Datos del paquete en el cuerpo de la solicitud
    db=Depends(get_mysql_session)  # Dependencia para obtener la sesión de base de datos
):
    # Crear una instancia del servicio de paquetes, inyectando la fábrica de MySQL
    service = PackageService(MySQLFactory(db))
    # Llamar al método para crear el paquete en la base de datos
    service.create_package(data)
    # Retornar un mensaje de éxito
    return {"message": "Package created"}

# Endpoint para listar todos los paquetes
@router.get(
    "/packages"  # Ruta del endpoint
)
def list_packages(
    db=Depends(get_mysql_session)  # Dependencia para obtener la sesión de base de datos
):
    # Crear una instancia del servicio de paquetes
    service = PackageService(MySQLFactory(db))
    # Retornar la lista de paquetes obtenida del servicio
    return service.list_packages()

# Endpoint para actualizar un paquete existente
@router.put(
    "/packages/{package_id}",  # Ruta con parámetro de ID de paquete
    dependencies=[Depends(JWTBearer())]  # Requiere autenticación JWT
)
def update_package(
    package_id: int,  # ID del paquete a actualizar
    data: PackageDTO,  # Datos actualizados del paquete
    db=Depends(get_mysql_session)  # Dependencia para obtener la sesión de base de datos
):
    # Crear una instancia del servicio de paquetes
    service = PackageService(MySQLFactory(db))
    # Llamar al método para actualizar el paquete y devolver el resultado
    return service.update_package(package_id, data)

# Endpoint para eliminar un paquete
@router.delete(
    "/packages/{package_id}",  # Ruta con parámetro de ID de paquete
    dependencies=[Depends(JWTBearer())]  # Requiere autenticación JWT
)
def delete_package(
    package_id: int,  # ID del paquete a eliminar
    db=Depends(get_mysql_session)  # Dependencia para obtener la sesión de base de datos
):
    # Crear una instancia del servicio de paquetes
    service = PackageService(MySQLFactory(db))
    # Llamar al método para eliminar el paquete y devolver el resultado
    return service.delete_package(package_id)
