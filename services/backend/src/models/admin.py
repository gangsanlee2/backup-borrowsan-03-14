from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin
from ..database import Base


class Admin(Base, TimestampMixin):
    __tablename__ = "admins"

    admin_id = Column(String(30), primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    token = Column(String(256))

    stands = relationship('Stand', back_populates='admin')
    umbrellas = relationship('Umbrella', back_populates='admin')
    articles = relationship('Article', back_populates='admin')
    users = relationship('User', back_populates='admin')
    rents = relationship('Rent', back_populates='admin')

    class Config:
        arbitrary_types_allowed = True
