from typing import List

import pymysql
from sqlalchemy.orm import Session
from abc import ABC
from ..bases.stand import StandBase
from ..models.stand import Stand
from ..schemas.stand import StandDTO

pymysql.install_as_MySQLdb()


class StandCrud(StandBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def add_stand(self, request_rent: StandDTO) -> str:
        pass

    def update_stand(self, request_rent: StandDTO) -> str:
        pass

    def delete_stand(self, request_rent: StandDTO) -> str:
        pass

    def fina_all_stands(self) -> List[Stand]:
        return self.db.query(Stand).all()

    def find_stand_by_id(self, request_rent: StandDTO) -> StandDTO:
        pass

    def count_all_stands(self) -> int:
        return self.db.query(Stand).count()

