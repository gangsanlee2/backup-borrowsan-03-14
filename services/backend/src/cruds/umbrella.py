from abc import ABC
from typing import List

import pymysql
from sqlalchemy.orm import Session

from ..bases.umbrella import UmbrellaBase
from ..models.umbrella import Umbrella
from ..schemas.umbrella import UmbrellaDTO

pymysql.install_as_MySQLdb()


class UmbrellaCrud(UmbrellaBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def add_umbrella(self, request_umbrella: UmbrellaDTO) -> str:
        umbrella = Umbrella(**request_umbrella.dict())
        if umbrella.image_url is not None:
            is_success = self.db.add(umbrella)
            self.db.commit()
            message = "SUCCESS: 우산 등록 완료"\
                if is_success != 0 else "FAILURE: 우산 등록 실패 / 알 수 없는 오류"
        else:
            message = "FAILURE: 우산 등록 실패"
        return message

    def update_umbrella(self, request_umbrella: UmbrellaDTO) -> str:
        pass

    def delete_umbrella(self, request_umbrella: UmbrellaDTO) -> str:
        pass

    def fina_all_umbrellas(self) -> List[Umbrella]:
        return self.db.query(Umbrella).all()

    def find_umbrella_by_id(self, request_umbrella: UmbrellaDTO) -> UmbrellaDTO:
        pass

    def count_all_umbrellas(self) -> int:
        return self.db.query(Umbrella).count()
