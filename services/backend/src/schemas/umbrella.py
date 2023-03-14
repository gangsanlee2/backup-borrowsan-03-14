from typing import Optional
from pydantic import BaseModel


class UmbrellaVO(BaseModel):
    class Config:
        orm_mode = True


class UmbrellaDTO(UmbrellaVO):
    umb_id: Optional[int]
    disrepair_rate: Optional[int]
    image_url: Optional[str]
    status: Optional[str]
    admin_id: Optional[str]
    stand_id: Optional[int]
