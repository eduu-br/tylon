from abc import ABC


class CredentialRepository(ABC):

    def execute(self, query): ...
