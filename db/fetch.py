import sqlite3 as sql

def get_transaction_db
    conn = sql.connect('db.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")

    transactions = c.fetchall()