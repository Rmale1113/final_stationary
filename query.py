import sqlite3

connection = sqlite3.connect("stationary.db")

cursor = connection.cursor()

rows = cursor.execute("select * from customers")
rows = cursor.fetchall()
rows1 = cursor.execute("select * from products")
rows1 = cursor.fetchall()
print(rows)
print(rows1)