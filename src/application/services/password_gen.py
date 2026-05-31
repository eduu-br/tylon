import random


class PasswordGenerator:

    def __init__(
        self,
        *,
        symbols: bool = False,
        length: int = 12,
        numbers: bool = False,
    ) -> None:
        self._chars = "qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM"
        if symbols:
            self._chars += "!@#$%&?/"
        if numbers:
            self._chars += "1234567890"
        self._length = length

    def generate(self):
        password = ""
        for _ in range(self._length):
            password += random.choice(self._chars)
        return password
