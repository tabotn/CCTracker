import os
import sqlite3 as sql
from temp_func import *
import sqlite3 as sql

def get_transactions_db():
    conn = sql.connect('db/db.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    trans = c.fetchall()
    return(trans)



def get_desired_action():
    action = input('What do you wan to do?\n 1. (R)ecord transaction?\n 2. (C)ange transaction?\n 3. (D)elete transaction?\n ')

    if action.upper() == 'R':
        record_transaction()
    elif action.upper() == 'C':
        change_transaction()
    elif action.upper() == 'D':
        delete_transaction()
    else:
        os.system('clear')
        print("Well thats not correct, let's start over. Chose R/C/D\n")
        get_desired_action()


def change_transaction():
    print('You chose "Change transaction"')

def delete_transaction():
    print('You chose "Delete transaction"')

def record_transaction():
    print("You chose 'Record transaction'")
    trans_id = int(input('id'))
    ccurrency = input('Which Coin?')
    date = input('which date?')
    t_type = input('Buy or Sell')
    pair = input('Which pair?')
    amount = float(input('How many coins?'))
    price = float(input('Value of coin?'))
    exchange = input('At which exchange did you buy?')
    cost = float(price) / float(amount)
    #print(f"You {t_type}ed {amount} of {coin.upper()} for {price} on {date}\n correct???")

    conn = sql.connect('db/db.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?)", (trans_id, date, t_type, coin, pair, amount, price, cost, exchange ))


