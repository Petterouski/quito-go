# Importamos la clase BaseModel de pydantic para crear modelos de datos que validan automáticamente
from pydantic import BaseModel
# Importamos la clase date del módulo datetime para manejar fechas
from datetime import date

# Definimos un modelo de datos para reservas utilizando pydantic
class ReservationDTO(BaseModel):
    # ID del usuario que realiza la reserva
    user_id: int
    # ID del paquete que se reserva
    package_id: int
    # Fecha en la que se realiza la reserva
    reservation_date: date
    # Cantidad de paquetes reservados
    quantity: int
