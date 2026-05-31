from abc import ABC, abstractmethod
from tylon.src.domain.entities.credential import Credential


class CredentialRepository(ABC):
    @abstractmethod
    def get_username(self, username: str) -> Credential | None: ...
