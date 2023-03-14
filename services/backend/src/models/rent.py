from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME as Datetime


class Rent(Base):

    __tablename__ = "rents"

    rent_id = Column(Integer, autoincrement=True, primary_key=True)
    disrepair = Column(Integer, nullable=False)
    rent_time = Column(Datetime, nullable=False)
    return_time = Column(Datetime, nullable=True)

    admin_id = Column(String(30), ForeignKey('admins.admin_id'))
    user_id = Column(String(30), ForeignKey('users.user_id'))
    umb_id = Column(Integer, ForeignKey('umbrellas.umb_id'))

    user = relationship('User', back_populates='rents')
    admin = relationship('Admin', back_populates='rents')
    umbrella = relationship('Umbrella', back_populates='rents')

    class Config:
        arbitrary_types_allowed = True
