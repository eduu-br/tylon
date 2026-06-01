from tylon.src.application.use_cases.authenticate_user import AuthenticateUserUseCase
from tylon.src.infrastructure.database.connection import (
    get_connection,
    close_connection,
)
from tylon.src.infrastructure.database.repositories.user_repository import (
    SQLiteUserRepository,
)
from tylon.src.infrastructure.crypto.hashing import Hasher

repo = SQLiteUserRepository(get_connection())
hasher = Hasher()
auth = AuthenticateUserUseCase(repo, hasher)

# auth.register_user("eduardo123", "102030")

print(auth.login_user("eduardo123", "102030"))

close_connection()
