from tylon.src.domain.value_objects.login_return_code import AuthReturnCode
from tylon.src.domain.value_objects.auth_type import Auth


class LoginViewmodel:

    def auth(
        self, auth_type: Auth, username: str, password: str
    ) -> list[AuthReturnCode]:
        if auth_type == Auth.LOGIN:
            return self.login(username, password)
        elif auth_type == Auth.REGISTER:
            return self.register(username, password)
        else:
            raise Exception("how did it get here")

    def login(self, username: str, password: str):
        ret = []
        if username == "" or len(username) < 3:
            ret.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            ret.append(AuthReturnCode.INVALID_PASSWORD)

        if ret:
            return ret

        # todo: logica de login
        ret.append(AuthReturnCode.SUCCESSFUL)
        return ret

    def register(self, username: str, password: str):
        ret = []
        if username == "" or len(username) < 3:
            ret.append(AuthReturnCode.INVALID_USERNAME)
        if password == "" or len(password) < 8:
            ret.append(AuthReturnCode.INVALID_PASSWORD)

        if ret:
            return ret

        # todo:logica de auth
        ret.append(AuthReturnCode.SUCCESSFUL)
        return ret
