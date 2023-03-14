from sqlalchemy.orm import relationship
from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Article(Base, TimestampMixin):

    __tablename__ = "articles"
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    text = Column(String(20), nullable=False)
    reference_id = Column(String(20), nullable=True)

    admin_id = Column(String(30), ForeignKey("admins.admin_id"), nullable=True)
    user_id = Column(String(30), ForeignKey("users.user_id"), nullable=True)

    user = relationship('User', back_populates='articles')
    admin = relationship('Admin', back_populates='articles')

    class Config:
        arbitrary_types_allowed = True
