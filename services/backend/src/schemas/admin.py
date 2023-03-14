from pydantic import BaseModel
from ..schemas.article import ArticleDTO
from ..schemas.rent import RentDTO
from ..schemas.stand import StandDTO
from ..schemas.umbrella import UmbrellaDTO
from ..schemas.user import UserDTO
from typing import List, Optional


class AdminDTO(BaseModel):
    admin_id: Optional[str]
    name: Optional[str]
    password: Optional[str]
    token: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True


class AdminDetail(AdminDTO):
    stands: List[StandDTO] = []

    articles: List[ArticleDTO] = []

    umbrellas: List[UmbrellaDTO] = []
    articles: List[ArticleDTO] = []

    users: List[UserDTO] = []
    rents: List[RentDTO] = []
