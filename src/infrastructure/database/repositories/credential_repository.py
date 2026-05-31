from src.domain.entities.credential import Credential
from src.domain.interfaces.repositories import CredentialRepository
from sqlite3 import Connection


class SQLiteCredentialRepository(CredentialRepository):

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def add_credential(self, credential: Credential):
        c = self._connection.cursor()
        c.execute(
            "INSERT INTO credentials VALUES (?,?,?,?,?,?,?,?)", credential.to_tuple()
        )
        self._connection.commit()
        c.close()

    def execute(self, query, params=()):
        c = self._connection.cursor()
        c.execute(query, params)
        self._connection.commit()
        c.close()
