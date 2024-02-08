import psycopg2
import sys
sys.path.append("/Users/razyesh/it-training-python-class/database")

dbname = "test_py"
user = "razyesh"
password = ""
host = "localhost"
port = "5432"

from db import DBConnection

new_db = DBConnection()
with new_db.connect_postgres(host=host, port=port, dbname=dbname, user=user, password=password) as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            email VARCHAR(100) UNIQUE
        );
    """)

    # Create Profile table with a foreign key referencing the User table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100),
            user_id INTEGER UNIQUE,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    """)

    rows = cursor.execute(
        """
        SELECT
            users.id,
            users.username,
            users.email,
            profiles.full_name
        FROM
            users
        JOIN
            profiles ON users.id = profiles.user_id;
        """
    )
    if rows:
        for row in rows:
            print(row)