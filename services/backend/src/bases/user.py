from abc import abstractmethod, ABCMeta
from typing import List

from ..models.user import User
from ..schemas.user import UserDTO, UserUpdate


class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def login(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def logout(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def update_user(self, request_user: UserUpdate) -> str: pass

    @abstractmethod
    def update_token(self, db_user: User, new_token: str) -> str: pass

    @abstractmethod
    def update_password(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def delete_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def find_all_users_ordered(self) -> List[User]: pass

    @abstractmethod
    def find_user_by_token(self, request_user: UserDTO) -> User: pass

    @abstractmethod
    def find_user_by_id(self, request_user: UserDTO) -> User: pass

    @abstractmethod
    def find_user_by_id_for_update(self, request_user: UserUpdate) -> User: pass

    @abstractmethod
    def find_user_by_email(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def find_all_users(self) -> List[User]: pass

    @abstractmethod
    def match_token(self, request_user: UserDTO) -> bool: pass

    @abstractmethod
    def match_token_for_modify(self, request_user: UserUpdate) -> bool: pass

    @abstractmethod
    def count_all_users(self) -> int: pass
