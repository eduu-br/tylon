from sqlite3 import Connection
from typing import Any
from tylon.src.domain.entities.user import User
from tylon.src.domain.interfaces.abc_user_repository import UserRepository


class SQLiteUserRepository(UserRepository):

    def __init__(self, connection: Connection, *, auto_commit: bool = True) -> None:
        self._connection = connection

        self._auto_commit = auto_commit

    def get_id(self, id: int) -> User | None:
        c = self._connection.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (id,))
        result = c.fetchall()
        c.close()
        if result:
            result = result[0]
            return User(result[0], result[1], result[2], result[3], result[4])
        else:
            return None

    def get_username(self, username: str) -> User | None:
        c = self._connection.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = c.fetchall()
        c.close()
        if result:
            result = result[0]
            return User(result[0], result[1], result[2], result[3], result[4])
        else:
            return None

    def add_user(self, username: str, password_hash: str) -> None:
        c = self._connection.cursor()
        c.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash),
        )
        if self._auto_commit:
            self.commit()
        c.close()

    def commit(self) -> None:
        self._connection.commit()
