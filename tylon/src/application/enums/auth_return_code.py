import enum


class AuthReturnCode(enum.Enum):
    SUCCESS = enum.auto()
    INVALID_USERNAME = enum.auto()
    INVALID_PASSWORD = enum.auto()
    LOGIN_INCORRECT_USERNAME = enum.auto()
    LOGIN_INCORRECT_PASSWORD = enum.auto()
    REGISTER_USERNAME_EXISTS = enum.auto()
    FAILED = enum.auto()
