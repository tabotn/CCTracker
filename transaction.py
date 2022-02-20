import pandas as pd
import sqlite3 as sql
import datetime

trans_conn = sql.connect("db/db.sqlite")
transactions = pd.read_sql_query("SELECT * from transactions", trans_conn)

print('Transactions are:\n')
print(transactions)

buys = transactions[(transactions.type == 'BUY')]

print("\nBuys are:\n")
print(buys)

sells = transactions[(transactions.type == 'SELL')]

print("\nSells are:\n")
print(sells)

start_date = transactions['date'].min() 

last_date = transactions['date'].max()

print(f"\nstarting date is: {start_date} and last date is: {last_date}")