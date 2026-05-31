class CredentialID:
    def __init__(self, value: int | str) -> None:
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"invalid id value: {value}")

        if value <= 0:
            raise ValueError(f"VaultID must be positive: {value}")

        self._id = value

    @property
    def value(self) -> int:
        return self._id

    def __eq__(self, other) -> bool:
        if not isinstance(other, CredentialID):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._id})"
