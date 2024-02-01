# import sqlite3
# conn = sqlite3.connect("test_db.db")
# cur = conn.cursor()
# try:
#     cur.execute("CREATE TABLE movie(name,release_date)")
# except sqlite3.OperationalError:
#     pass
# # cur.execute("INSERT INTO movie VALUES('Abcd', '2023-10-11')")
# try:
#     cur.execute("INSERT INTO movie VALUES('Abcdefg', '2023-10-11')")
#     cur.execute("SELECT * from movie")
#     cur.execute("CREATE TABLE movie(name,release_date)")
#     conn.commit()
# except Exception:
#     conn.rollback()

# print(cur.fetchall())
# conn.close()

import sqlite3
from contextlib import contextmanager

class DBConnection:
    def __init__(self, db_file):
        self.db_file = db_file

    @contextmanager
    def connect(self):
        """ Context manager for database connections. """
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

# Usage example
db = DBConnection("test_db.db")

with db.connect() as cursor:
    cursor.execute("INSERT INTO movie (name, release_date) VALUES (?, ?)", ("JKL", "2022-01-01"))