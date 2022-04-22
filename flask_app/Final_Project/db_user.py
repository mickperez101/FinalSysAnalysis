import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE Accounts (username TEXT, password TEXT, email TEXT)")

conn.close()

print("Table created")