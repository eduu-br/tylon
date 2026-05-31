from tylon.src.infrastructure.database.repositories.user_repository import (
    SQLiteUserRepository,
)
from tylon.src.infrastructure.database.connection import get_connection
from tylon.src.application.enums.auth_return_code import AuthReturnCode
from tylon.src.infrastructure.crypto.hashing import Hashing


class AuthenticateUserUseCase:
    def __init__(self) -> None:
        self._repo = SQLiteUserRepository(get_connection())
        self._hasher = Hashing()

    def register_user(self, username: str, password: str, /):
        if self._repo.get_username(username) is not None:
            return AuthReturnCode.REGISTER_USERNAME_EXISTS
        self._repo.add_user(username, self._hasher.hash(password))
        return AuthReturnCode.SUCCESS

    def login_user(self, username: str, password: str, /):
        user = self._repo.get_username(username)
        if user is None:
            return AuthReturnCode.LOGIN_INCORRECT_USERNAME
        if self._hasher.verify(user.password_hash, password):
            return AuthReturnCode.SUCCESS
        else:
            return AuthReturnCode.LOGIN_INCORRECT_PASSWORD
