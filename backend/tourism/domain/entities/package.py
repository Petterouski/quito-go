# Define la entidad del dominio, que representa un paquete turístico
class Package:
    def __init__(self, id, destination, duration_days, price, capacity):
        self.id = id
        self.destination = destination
        self.duration_days = duration_days
        self.price = price
        self.capacity = capacity
