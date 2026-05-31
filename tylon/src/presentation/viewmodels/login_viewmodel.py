from tylon.src.application.enums.auth_return_code import AuthReturnCode
from tylon.src.application.enums.auth_mode import AuthMode
from tylon.src.application.use_cases.authenticate_user import AuthenticateUserUseCase


class AuthViewmodel:

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
        ret = []
        if username == "" or len(username) < 3:
            ret.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            ret.append(AuthReturnCode.INVALID_PASSWORD)

        if ret:
            return ret

        # todo: logica de login
        ret.append(AuthReturnCode.SUCCESS)
        return ret

    def register(self, username: str, password: str):
        ret = []
        if username == "" or len(username) < 3:
            ret.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            ret.append(AuthReturnCode.INVALID_PASSWORD)

        if ret:
            return ret

        # todo:logica de register
        ret.append(AuthReturnCode.SUCCESS)
        return ret
