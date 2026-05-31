import sqlite3
import os

db_path = os.getenv("LOCALAPPDATA")
if db_path is None:
    raise Exception("idk how")
else:
    db_path += "\\.tylon\\tylon.db"

with open(".\\src\\infrastructure\\database\\schema.sql") as f:
    schema = f.read()

connection = None


def get_connection():
    global connection
    if db_path is None:
        raise Exception("idk how this happened")

    if not os.path.exists(db_path):
        connection = sqlite3.connect(db_path)
        c = connection.cursor()
        c.execute(schema)
        connection.commit()
        c.close()
    return connection


def close_connection():
    global connection
    if connection is not None:
        connection.close()


print(get_connection())
