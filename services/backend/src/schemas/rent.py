from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RentVO(BaseModel):
    class Config:
        orm_mode = True


class RentDTO(RentVO):
    rent_id: Optional[int]
    disrepair: Optional[int]
    rent_time: Optional[datetime]
    return_time: Optional[datetime]
    admin_id: Optional[str]
    user_id: Optional[str]
    umb_id: Optional[int]
