# Importa la clase Reservation del módulo de entidades del dominio
from domain.entities.reservation import Reservation
# Importa la interfaz ReservationRepository que define los métodos que debe implementar el DAO
from domain.interfaces.reservation_repository import ReservationRepository
# Importa ObjectId para manipular identificadores únicos en MongoDB
from bson import ObjectId

class MongoReservationDAO(ReservationRepository):
    def __init__(self, db):
        # Inicializa la colección de reservas en la base de datos MongoDB
        self.collection = db["reservations"]

    def create(self, reservation: Reservation):
        """
        Crea una nueva reserva en la base de datos.
        Args:
            reservation (Reservation): La instancia de reserva a guardar.
        """
        # Construye el documento a partir de la entidad Reservation
        doc = self._build_insert_document(reservation)
        # Inserta el documento en la colección de reservas
        self.collection.insert_one(doc)

    def delete(self, reservation_id: str):
        """
        Elimina una reserva de la base de datos por su ID.
        Args:
            reservation_id (str): El identificador único de la reserva a eliminar.
        """
        # Construye el filtro para localizar la reserva por su ObjectId
        filter_query = self._build_delete_filter(reservation_id)
        # Ejecuta la eliminación del documento que coincida con el filtro
        self.collection.delete_one(filter_query)

    # -----------------------------------
    # Métodos privados para construir datos
    # -----------------------------------

    def _build_insert_document(self, reservation: Reservation):
        """
        Construye el diccionario (documento) a insertar en MongoDB a partir de una reserva.
        Args:
            reservation (Reservation): La reserva que se desea guardar.
        Returns:
            dict: Documento formateado para MongoDB.
        """
        return {
            "user_id": reservation.user_id,
            "package_id": reservation.package_id,
            # Convierte la fecha de reserva a formato ISO para almacenamiento
            "reservation_date": reservation.reservation_date.isoformat(),
            "quantity": reservation.quantity
        }

    def _build_delete_filter(self, reservation_id: str):
        """
        Construye el filtro para localizar la reserva por su ObjectId en MongoDB.
        Args:
            reservation_id (str): La cadena que representa el ObjectId de la reserva.
        Returns:
            dict: Diccionario con el filtro para la consulta.
        """
        return {"_id": ObjectId(reservation_id)}
