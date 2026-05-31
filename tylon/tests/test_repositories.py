from tylon.src.infrastructure.database.repositories.user_repository import (
    SQLiteUserRepository,
)
from tylon.src.infrastructure.database.repositories.credential_repository import (
    SQLiteCredentialRepository,
)
from tylon.src.infrastructure.database.connection import (
    get_connection,
    close_connection,
)

users = SQLiteUserRepository(get_connection())
credentials = SQLiteCredentialRepository(get_connection())

credentials.add_credential(123213, "valorant", "edu.br", "osadfy79sd6")
print(credentials.get_username("edu.br"))
# print(users.get_username("eduardo"))

close_connection()
