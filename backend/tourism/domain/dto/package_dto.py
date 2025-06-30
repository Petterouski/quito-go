from pydantic import BaseModel

# Define un Data Transfer Object (DTO) que valida la entrada de datos del usuario
class PackageDTO(BaseModel):
    id: int | None = None
    destination: str
    duration_days: int
    price: float
    capacity: int # Capacidad de personas
