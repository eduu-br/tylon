from .credential import Credential
from typing import overload


class Vault:

    def __init__(self) -> None:
        self._credentials: list[Credential] = []

    def add_credential(self, credential: Credential, /) -> None:
        if not isinstance(credential, Credential):
            raise TypeError(
                f"invalid argument type: {type(credential)}, expected {Credential.__class__}"
            )
        self._credentials.append(credential)

    def remove_credential(self, credential_id: int, /) -> None:
        for cr in self._credentials:
            if cr.id == credential_id:
                self._credentials.remove(cr)
                return
        raise ValueError(f"invalid credential id")

    def search(self, id: int):

        for cr in self._credentials:
            if cr.id == id:
                return cr
