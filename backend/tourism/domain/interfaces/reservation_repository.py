from abc import ABC, abstractmethod
from domain.entities.reservation import Reservation

class ReservationRepository(ABC):
    @abstractmethod
    def create(self, reservation: Reservation): pass

    @abstractmethod
    def delete(self, reservation_id: str): pass
