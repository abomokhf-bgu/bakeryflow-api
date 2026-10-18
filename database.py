import sqlite3
connection = sqlite3.connect("bakery.db")

cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL, stock INTEGER NOT NULL)""")
connection.commit()
connection.close()
print("Products table created successfully!")