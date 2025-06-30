# Importación de dependencias necesarias de FastAPI y otros módulos del proyecto
from fastapi import APIRouter, Depends

# Importación del Data Transfer Object (DTO) para reservas
from domain.dto.reservation_dto import ReservationDTO

# Función para obtener la conexión a MongoDB desde la configuración
from config.mongo_config import get_mongo_client

# Factoría para crear instancias del repositorio MongoDB
from infrastructure.factories.mongo_factory import MongoFactory

# Servicio que contiene la lógica de negocio relacionada con reservas
from application.services.reservation_service import ReservationService

# Creación de un router de FastAPI para agrupar las rutas relacionadas con reservas
router = APIRouter()

@router.post("/reservations")
def reserve_package(data: ReservationDTO):
    """
    Endpoint para reservar un paquete.
    Recibe los datos de reserva en el cuerpo de la solicitud, en formato ReservationDTO.
    """
    # Obtiene la instancia del cliente MongoDB
    db = get_mongo_client()
    # Crea una instancia del servicio de reserva, pasando la fábrica de MongoDB
    service = ReservationService(MongoFactory(db))
    # Llama al método del servicio para reservar el paquete con los datos recibidos
    service.reserve_package(data)
    # Devuelve un mensaje de éxito
    return {"message": "Package reserved successfully"}

@router.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: str):
    """
    Endpoint para cancelar una reserva existente.
    Recibe el ID de la reserva a cancelar como parámetro de la URL.
    """
    # Obtiene la instancia del cliente MongoDB
    db = get_mongo_client()
    # Crea una instancia del servicio de reserva
    service = ReservationService(MongoFactory(db))
    # Llama al método del servicio para cancelar la reserva usando el ID proporcionado
    service.cancel_reservation(reservation_id)
    # Devuelve un mensaje de confirmación
    return {"message": "Reservation cancelled"}
