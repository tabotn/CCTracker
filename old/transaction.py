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
#print(BTC)
#
index = 0
ind = index + 1

ceiling = transactions.id.max()
transactions[0:ind]

BTC_sum = BTC.value.sum()


if transactions.iloc[index]['type'] == 'BUY':
    
    new_transaction = pd.DataFrame(data={'date': [transactions.iloc[index]['date']], })
    print(new_transaction)
#print(transactions[0:ind])
