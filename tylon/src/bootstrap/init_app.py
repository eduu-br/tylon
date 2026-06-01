from tylon.src.infrastructure.storage.app_directory import ensure_app_directory
from tylon.src.infrastructure.database.initializer import ensure_database
from tylon.src.infrastructure.crypto.hashing import Hasher


def init():

    ensure_app_directory()
    ensure_database()
