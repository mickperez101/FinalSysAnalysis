import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE Product_Entry (product TEXT, description TEXT, quantity INTEGER, checkin TEXT)")

conn.close()

print("Table created")