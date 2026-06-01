class SessionManager:
    def __init__(self):
        self._user = None
        self._encryption_key = None

    @property
    def encryption_key(self):
        return self._encryption_key

    @property
    def user(self):
        return self._user

    def is_authenticated(self) -> bool:
        return self._user is not None

    def login(self, user, encryption_key) -> None:
        self._user = user
        self._encryption_key = encryption_key

    def logout(self) -> None:
        self._user = None
        self._encryption_key = None
