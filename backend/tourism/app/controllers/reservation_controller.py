from fastapi import APIRouter, Depends
from domain.dto.reservation_dto import ReservationDTO
from config.mongo_config import get_mongo_client
from infrastructure.factories.mongo_factory import MongoFactory
from application.services.reservation_service import ReservationService

router = APIRouter()

@router.post("/reservations")
def reserve_package(data: ReservationDTO):
    db = get_mongo_client()
    service = ReservationService(MongoFactory(db))
    service.reserve_package(data)
    return {"message": "Package reserved successfully"}

@router.delete("/reservations/{reservation_id}")
def cancel_reservation(reservation_id: str):
    db = get_mongo_client()
    service = ReservationService(MongoFactory(db))
    service.cancel_reservation(reservation_id)
    return {"message": "Reservation cancelled"}

