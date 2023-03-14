from abc import ABCMeta, abstractmethod
from typing import List

from ..models.stand import Stand
from ..schemas.stand import StandDTO


class StandBase(metaclass=ABCMeta):

    @abstractmethod
    def add_stand(self, request_rent: StandDTO) -> str: pass

    @abstractmethod
    def update_stand(self, request_rent: StandDTO) -> str: pass

    @abstractmethod
    def delete_stand(self, request_rent: StandDTO) -> str: pass

    @abstractmethod
    def fina_all_stands(self) -> List[Stand]: pass

    @abstractmethod
    def find_stand_by_id(self, request_rent: StandDTO) -> StandDTO: pass

    @abstractmethod
    def count_all_stands(self) -> int: pass
