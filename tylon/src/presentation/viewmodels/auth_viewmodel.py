from tylon.src.application.enums.auth_return_code import AuthReturnCode
from tylon.src.presentation.viewmodels.auth_mode import AuthMode
from tylon.src.application.use_cases.authenticate_user import AuthenticateUserUseCase
from tylon.src.domain.interfaces.abc_user_repository import UserRepository
from tylon.src.application.session.session_manager import SessionManager
from tylon.src.infrastructure.crypto.hashing import Hasher


class AuthViewmodel:

    def __init__(
        self,
        user_repository: UserRepository,
        hasher: Hasher,
        session_manager: SessionManager,
    ) -> None:
        self._user_repository = user_repository
        self._session_manager = session_manager
        self.auth_use_case = AuthenticateUserUseCase(user_repository, hasher)

    def auth(
        self, auth_type: AuthMode, username: str, password: str
    ) -> list[AuthReturnCode]:
        if auth_type == AuthMode.LOGIN:
            return self.login(username, password)
        elif auth_type == AuthMode.REGISTER:
            return self.register(username, password)
        else:
            return [AuthReturnCode.FAILED]

    def login(self, username: str, password: str):
        code_stack = []
        if username == "" or len(username) < 3:
            code_stack.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            code_stack.append(AuthReturnCode.INVALID_PASSWORD)

        if code_stack:
            return code_stack

        result = self.auth_use_case.login_user(username, password)

        if result == AuthReturnCode.SUCCESS:
            user = self._user_repository.get_username(username)
            if user is None:
                return [AuthReturnCode.FAILED]
            self._session_manager.login(user)

        code_stack.append(result)
        return code_stack

    def register(self, username: str, password: str):
        code_stack = []
        if username == "" or len(username) < 3:
            code_stack.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            code_stack.append(AuthReturnCode.INVALID_PASSWORD)

        if code_stack:
            return code_stack

        result = self.auth_use_case.register_user(username, password)

        code_stack.append(result)
        return code_stack
