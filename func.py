import os
import sqlite3 as sql
from temp_func import *
import sqlite3 as sql

def get_transaction_db():
    conn = sql.connect('db/db.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    trans = c.fetchall()


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

def record_transaction():
    print("You chose 'Record transaction'")

def change_transaction():
    print('You chose "Change transaction"')

def delete_transaction():
    print('You chose "Delete transaction"')

get_transaction_db()
