import sqlite3

conn = sqlite3.connect("data/database.sqlite")
# conn.row_factory = sqlite3.Row
c = conn.cursor()
# c.execute("SELECT * FROM League")
# rows = c.fetchall()
# for row in rows:
#     print(row['name'])

c.execute("SELECT * FROM Country WHERE Country.id = 1")
row = c.fetchone()
print(row)
print(row[0], '-' ,row[1])

# c.execute("SELECT * FROM Country")
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)