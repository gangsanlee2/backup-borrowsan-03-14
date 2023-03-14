from typing import List, Optional
from pydantic import BaseModel
from ..schemas.article import ArticleDTO
from ..schemas.rent import RentDTO


class UserVO(BaseModel):
    class Config:
        orm_mode = True


class UserDTO(UserVO):
    user_id: Optional[str]
    age: Optional[str]
    address: Optional[str]
    most_use_loc: Optional[str]
    cur_lat: Optional[str]
    cur_lng: Optional[str]
    birth: Optional[str]
    grade: Optional[str]
    pay_info: Optional[str]
    password: Optional[str]
    email: Optional[str]
    gender: Optional[str]
    token: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class UserList(UserVO):
    user_id: Optional[str]
    age: Optional[str]
    address: Optional[str]
    most_use_loc: Optional[str]
    cur_lat: Optional[str]
    cur_lng: Optional[str]
    birth: Optional[str]
    grade: Optional[str]
    pay_info: Optional[str]
    password: Optional[str]
    email: Optional[str]
    gender: Optional[str]
    token: Optional[str]


class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []
    rents: List[RentDTO] = []


class UserUpdate(BaseModel):
    user_id: Optional[str]
    address: Optional[str]
    most_use_loc: Optional[str]
    cur_lat: Optional[str]
    cur_lng: Optional[str]
    grade: Optional[str]
    pay_info: Optional[str]
    gender: Optional[str]
    token: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True