import enum


class AuthReturnCode(enum.Enum):
    SUCCESSFUL = enum.auto()
    INVALID_USERNAME = enum.auto()
    INVALID_PASSWORD = enum.auto()
    INCORRECT_PASSWORD = enum.auto()
    INCORRECT_USERNAME = enum.auto()
    FAILED = enum.auto()
