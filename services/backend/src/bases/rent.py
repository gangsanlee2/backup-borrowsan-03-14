from abc import ABCMeta, abstractmethod
from typing import List
from ..models.rent import Rent
from ..schemas.rent import RentDTO


class RentBase(metaclass=ABCMeta):

    @abstractmethod
    def add_rent(self, request_rent: RentDTO) -> str: pass

    @abstractmethod
    def update_rent(self, request_rent: RentDTO) -> str: pass

    @abstractmethod
    def delete_rent(self, request_rent: RentDTO) -> str: pass

    @abstractmethod
    def fina_all_rents(self) -> List[Rent]: pass

    @abstractmethod
    def find_rent_by_id(self, request_rent: RentDTO) -> RentDTO: pass

    @abstractmethod
    def count_all_rents(self) -> int: pass
