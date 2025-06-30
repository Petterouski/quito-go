from domain.dto.reservation_dto import ReservationDTO
from domain.entities.reservation import Reservation

class ReservationService:
    def __init__(self, factory):
        self.dao = factory.create_reservation_dao()

    def reserve_package(self, dto: ReservationDTO):
        reservation = Reservation(**dto.dict())
        self.dao.create(reservation)

    def cancel_reservation(self, reservation_id: str):
        self.dao.delete(reservation_id)
