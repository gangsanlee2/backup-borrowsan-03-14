from typing import Optional
from pydantic import BaseModel


class StandVO(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class StandDTO(StandVO):
    stand_id: Optional[int]
    district: Optional[str]
    latitude: Optional[int]
    longitude: Optional[int]
    admin_id: Optional[str]
