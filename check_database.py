import sqlite3

connection = sqlite3.connect("bakery.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
print(rows)
connection.close()