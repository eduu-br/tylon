from abc import ABC, abstractmethod
from typing import Any
from sqlite3 import Connection
from tylon.src.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def __init__(self, connection: Connection, *, auto_commit: bool) -> None: ...
    @abstractmethod
    def get_username(self, username: str) -> User | None: ...
    @abstractmethod
    def get_id(self, id: int) -> User | None: ...
    @abstractmethod
    def add_user(self, username: str, password: str): ...
    @abstractmethod
    def commit(self) -> None: ...
