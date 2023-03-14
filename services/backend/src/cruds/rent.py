from typing import List

import pymysql
from sqlalchemy.orm import Session
from abc import ABC
from ..bases.rent import RentBase
from ..models.rent import Rent
from ..schemas.rent import RentDTO

pymysql.install_as_MySQLdb()


class RentCrud(RentBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def add_rent(self, request_rent: RentDTO) -> str:
        pass

    def update_rent(self, request_rent: RentDTO) -> str:
        pass

    def delete_rent(self, request_rent: RentDTO) -> str:
        pass

    def fina_all_rents(self) -> List[Rent]:
        return self.db.query(Rent).all()

    def find_rent_by_id(self, request_rent: RentDTO) -> RentDTO:
        pass

    def count_all_rents(self) -> int:
        return self.db.query(Rent).count()
