from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class Hashing:

    def __init__(self) -> None:
        self._hasher = PasswordHasher()

    def hash(self, password: str, /):
        return self._hasher.hash(password)

    def verify(self, hash: str, password: str, /):
        try:
            return self._hasher.verify(hash, password)
        except VerifyMismatchError:
            return False
