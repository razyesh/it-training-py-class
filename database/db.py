import sqlite3
conn = sqlite3.connect("test_db.db")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE movie(name,release_date)")
except sqlite3.OperationalError:
    pass
# cur.execute("INSERT INTO movie VALUES('Abcd', '2023-10-11')")
try:
    cur.execute("INSERT INTO movie VALUES('Abcdefg', '2023-10-11')")
    cur.execute("SELECT * from movie")
    cur.execute("CREATE TABLE movie(name,release_date)")
    conn.commit()
except Exception:
    conn.rollback()

print(cur.fetchall())
conn.close()

import sqlite3
import psycopg2
from pymongo import MongoClient
import mysql.connector
from contextlib import contextmanager

class DBConnection:
    def __init__(self, db_file=None):
        self.db_file = db_file

    @contextmanager
    def connect_sqlite(self):
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

    @contextmanager
    def connect_postgres(self, host, port, dbname, user, password):
        """ Context manager for database connections. """
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @contextmanager
    def connect_mysql(self, host, port, dbname, user, password):
        """ Context manager for database connections. """
        connection = mysql.connector.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    @contextmanager
    def connect_mongo(self, host, port, dbname, user, password):
        """ Context manager for database connections. """
        client = MongoClient(
            username=user,
            password=password,
            host=host,
            port=port,
            connect=False
        )
        db = client[dbname]
        session = client.start_session()
        session.start_transaction()
        try:
            yield db  # Provide the database connection to the caller
            # Commit the transaction
            session.commit_transaction()
        finally:
            session.end_session()

# Usage example
db = DBConnection("test_db.db")

with db.connect_sqlite() as cursor:
    cursor.execute("INSERT INTO movie (name, release_date) VALUES (?, ?)", ("JKL", "2022-01-01"))