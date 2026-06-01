from tylon.src.domain.interfaces.abc_user_repository import UserRepository
from tylon.src.application.enums.auth_return_code import AuthReturnCode
from tylon.src.infrastructure.crypto.hashing import Hasher


class AuthenticateUserUseCase:
    def __init__(self, user_repository: UserRepository, hasher: Hasher) -> None:
        self._repo = user_repository
        self._hasher = hasher

    def register_user(self, username: str, password: str, /):
        if self._repo.get_username(username) is not None:
            return AuthReturnCode.REGISTER_USERNAME_EXISTS
        self._repo.add_user(username, self._hasher.hash(password))
        return AuthReturnCode.SUCCESS

    def login_user(self, username: str, password: str, /):
        user = self._repo.get_username(username)
        if user is None:
            return AuthReturnCode.LOGIN_INCORRECT_USERNAME
        if self._hasher.verify(password, user.password_hash):
            return AuthReturnCode.SUCCESS
        else:
            return AuthReturnCode.LOGIN_INCORRECT_PASSWORD
