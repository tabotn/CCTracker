import pandas as pd
import sqlite3 as sql
import datetime

#connect to sqlite db
trans_conn = sql.connect("db/db.sqlite")
transactions = pd.read_sql_query("SELECT * from transactions", trans_conn)

#create separate df of all buys and sell
buys = transactions[(transactions.type == 'BUY')]
sells = transactions[(transactions.type == 'SELL')]

# create df headers for BTC portfolio
BTC = pd.DataFrame(data={'date': ['2022-01-01'], 'amount': [0], 'value': [0], 'gav': [0], 'profit/loss': [0]})

#
ind = 1
transactions[0:ind]


print(transactions[0:ind].type)
