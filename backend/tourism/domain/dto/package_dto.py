from pydantic import BaseModel

# Definición de un Data Transfer Object (DTO) utilizando Pydantic para validar la entrada de datos
class PackageDTO(BaseModel):
    # Identificador único del paquete, puede ser None si aún no se ha asignado
    id: int | None = None

    # Destino del paquete (por ejemplo, ciudad o país)
    destination: str

    # Duración del paquete en días
    duration_days: int

    # Precio del paquete en la moneda correspondiente
    price: float

    # Capacidad máxima de personas que pueden reservar el paquete
    capacity: int  # Capacidad de personas
