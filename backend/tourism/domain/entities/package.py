# Define la clase que representa una entidad del dominio, en este caso, un paquete turístico
class Package:
    def __init__(self, id, destination, duration_days, price, capacity):
        """
        Inicializa una instancia de la clase Package.

        :param id: Identificador único del paquete turístico.
        :param destination: Destino del paquete turístico.
        :param duration_days: Duración del paquete en días.
        :param price: Precio del paquete.
        :param capacity: Capacidad máxima de personas para el paquete.
        """
        self.id = id  # ID único del paquete
        self.destination = destination  # Destino del paquete
        self.duration_days = duration_days  # Duración en días
        self.price = price  # Precio del paquete
        self.capacity = capacity  # Capacidad máxima de personas
