from src.infrastructure.storage.app_directory import ensure_app_directory
from src.infrastructure.database.initializer import ensure_database


def init():
    ensure_app_directory()
    ensure_database()
