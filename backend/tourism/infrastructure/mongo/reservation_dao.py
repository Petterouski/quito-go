from domain.entities.reservation import Reservation
from domain.interfaces.reservation_repository import ReservationRepository
from bson import ObjectId

class MongoReservationDAO(ReservationRepository):
    def __init__(self, db):
        self.collection = db["reservations"]

    def create(self, reservation: Reservation):
        doc = self._build_insert_document(reservation)
        self.collection.insert_one(doc)

    def delete(self, reservation_id: str):
        filter_query = self._build_delete_filter(reservation_id)
        self.collection.delete_one(filter_query)

    # ------------------------------
    # Métodos privados encapsulados
    # ------------------------------

    def _build_insert_document(self, reservation: Reservation):
        return {
            "user_id": reservation.user_id,
            "package_id": reservation.package_id,
            "reservation_date": reservation.reservation_date.isoformat(),
            "quantity": reservation.quantity
        }

    def _build_delete_filter(self, reservation_id: str):
        return {"_id": ObjectId(reservation_id)}
