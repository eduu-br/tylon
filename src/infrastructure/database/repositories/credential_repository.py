# from src.domain.interfaces.repositories import CredentialRepository
# import sqlite3


# class SQLiteCredentialRepository(CredentialRepository):

#     def __init__(self, db_path) -> None:
#         self._db_path = db_path

#     def execute(self, query, params=()):
#         with sqlite3.connect(self._db_path) as db:
#             cursor = db.cursor()
#             cursor.execute(query, params)
#             cursor.close()
#             db.commit()
