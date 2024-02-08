# Relational vs Non-relational database 
# connect mysql database on your own

import sqlite3

conection_ = sqlite3.connect("employee.db")
cur = conection_.cursor()

try:
    cur.execute("CREATE TABLE profile (name, age, department)")
except sqlite3.OperationalError:
    pass
cur.execute("INSERT INTO profile VALUES ('Ram', '21', 'Science')")

conection_.commit()

conection_.close()