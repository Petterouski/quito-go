# Importamos los Data Transfer Objects (DTO) y las entidades del dominio necesarias
from domain.dto.reservation_dto import ReservationDTO
from domain.entities.reservation import Reservation

class ReservationService:
    """
    Servicio responsable de gestionar las operaciones relacionadas con reservas,
    como crear y cancelar reservas.
    """

    def __init__(self, factory):
        """
        Inicializa la instancia de ReservationService con una fábrica que crea
        el Data Access Object (DAO) para reservas.
        
        :param factory: Objeto que proporciona el método para crear el DAO de reservas
        """
        self.dao = factory.create_reservation_dao()

    def reserve_package(self, dto: ReservationDTO):
        """
        Crea una reserva basada en un DTO de reserva y la guarda en la base de datos.
        
        :param dto: Objeto ReservationDTO que contiene los datos de la reserva
        """
        # Convierte el DTO en una entidad de reserva utilizando unpacking de diccionario
        reservation = Reservation(**dto.dict())
        # Guarda la reserva en la base de datos mediante el DAO
        self.dao.create(reservation)

    def cancel_reservation(self, reservation_id: str):
        """
        Cancela una reserva existente identificada por su ID.
        
        :param reservation_id: Cadena que representa el identificador de la reserva a cancelar
        """
        # Elimina la reserva de la base de datos mediante el DAO
        self.dao.delete(reservation_id)
