import enum


class PasswordStrength(enum.Enum):
    WEAK = enum.auto()
    MEDIUM = enum.auto()
    STRONG = enum.auto()
