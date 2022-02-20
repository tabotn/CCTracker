import sqlite3 as sql

conn = sql.connect('db.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM transactions")

data = c.fetchall()



print(data)