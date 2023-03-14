from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChatVO(BaseModel):
    class Config:
        orm_mode = True


class ChatDTO(ChatVO):
    message: Optional[str]
