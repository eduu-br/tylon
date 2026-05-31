from tylon.src.domain.entities.credential import Credential
from tylon.src.domain.entities.user import User
from tylon.src.domain.interfaces.abc_credential_repositories import CredentialRepository
from sqlite3 import Connection


class SQLiteCredentialRepository(CredentialRepository):

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def get_username(self, username: str) -> Credential | None:
        c = self._connection.cursor()
        c.execute("SELECT * FROM credentials WHERE username = ?", (username,))
        result = c.fetchall()

        if result:
            result = result[0]
            return Credential(
                result[0],
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
                result[6],
                result[7],
            )
        else:
            return None

    def add_credential(
        self,
        vault_id: int,
        app: str,
        username: str,
        password_encrypted: str,
        notes: str = "",
        /,
    ):
        c = self._connection.cursor()
        c.execute(
            "INSERT INTO credentials (vault_id, app, username, password_encrypted, notes) VALUES (?, ?, ?, ?, ?)",
            (vault_id, app, username, password_encrypted, notes if notes else None),
        )
        self._connection.commit()
        c.close()
