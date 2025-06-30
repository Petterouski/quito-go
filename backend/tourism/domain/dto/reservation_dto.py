from pydantic import BaseModel
from datetime import date

class ReservationDTO(BaseModel):
    user_id: int
    package_id: int
    reservation_date: date
    quantity: int
