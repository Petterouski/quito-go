from abc import ABC, abstractmethod
from domain.entities.reservation import Reservation

class ReservationRepository(ABC):
    """
    Interfaz abstracta para el repositorio de reservas.
    Define los métodos que cualquier implementación concreta debe ofrecer
    para gestionar las reservas en el sistema.
    """

    @abstractmethod
    def create(self, reservation: Reservation):
        """
        Crea una nueva reserva en el sistema.
        
        Args:
            reservation (Reservation): La instancia de reserva que se desea crear.
        """
        pass

    @abstractmethod
    def delete(self, reservation_id: str):
        """
        Elimina una reserva existente del sistema mediante su identificador.
        
        Args:
            reservation_id (str): El identificador único de la reserva a eliminar.
        """
        pass # La implementación concreta será proporcionada en las clases derivadas
