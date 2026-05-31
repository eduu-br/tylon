import os
from .connection import get_connection

db_path = os.getenv("LOCALAPPDATA") + "\\.tylon\\tylon.db"  # type: ignore

with open(".\\tylon\\src\\infrastructure\\database\\schema.sql") as f:
    schema = f.read()


def ensure_database():
    if not os.path.exists(db_path):
        connection = get_connection()
        c = connection.cursor()
        c.executescript(schema)
        connection.commit()
        c.close()
