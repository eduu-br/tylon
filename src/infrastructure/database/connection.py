import sqlite3
import os

db_path = os.getenv("LOCALAPPDATA")
if db_path is None:
    raise Exception("idk how")
else:
    db_path += "\\.tylon\\tylon.db"


connection = None


def get_connection():
    global connection
    if db_path is None:
        raise Exception("idk how this happened")
    if connection is None:
        connection = sqlite3.connect(db_path)
    return connection


def close_connection():
    global connection
    if connection is not None:
        connection.close()
