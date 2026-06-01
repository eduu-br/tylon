from tylon.src.domain.entities.user import User


class SessionManager:
    def __init__(self) -> None:
        self._user: User | None = None
        self._encryption_key: bytes | None = None

    @property
    def encryption_key(self) -> bytes | None:
        return self._encryption_key

    @property
    def user(self) -> User | None:
        return self._user

    def is_authenticated(self) -> bool:
        return self._user is not None

    def login(self, user: User, encryption_key: bytes | None = None) -> None:
        self._user = user
        self._encryption_key = encryption_key

    def logout(self) -> None:
        self._user = None
        self._encryption_key = None
