# Definición de la clase Reservation que representa una reserva realizada por un usuario
class Reservation:
    def __init__(self, user_id, package_id, reservation_date, quantity):
        """
        Constructor de la clase Reservation.
        
        Parámetros:
        - user_id (int o str): Identificador único del usuario que realiza la reserva.
        - package_id (int o str): Identificador del paquete o producto reservado.
        - reservation_date (str o datetime): Fecha en que se realiza la reserva.
        - quantity (int): Cantidad de unidades reservadas.
        """
        # Asignación del identificador del usuario a un atributo de la instancia
        self.user_id = user_id
        # Asignación del identificador del paquete a un atributo de la instancia
        self.package_id = package_id
        # Asignación de la fecha de reserva a un atributo de la instancia
        self.reservation_date = reservation_date
        # Asignación de la cantidad reservada a un atributo de la instancia
        self.quantity = quantity
