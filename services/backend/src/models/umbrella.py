from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Umbrella(Base):

    __tablename__ = "umbrellas"
    umb_id = Column(Integer, autoincrement=True, primary_key=True)
    disrepair_rate = Column(Integer, nullable=False)
    image_url = Column(String(50), nullable=False)
    status = Column(String(10), nullable=False)

    stand_id = Column(Integer, ForeignKey('stands.stand_id'))
    admin_id = Column(String(30), ForeignKey('admins.admin_id'), nullable=True)

    rents = relationship('Rent', back_populates='umbrella')
    admin = relationship('Admin', back_populates='umbrellas')
    stand = relationship('Stand', back_populates='umbrellas')

    class Config:
        arbitrary_types_allowed = True
