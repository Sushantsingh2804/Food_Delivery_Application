from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("fooddeliveryapp.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'RESTAURANT'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE RESTAURANT(
                        RESTAURANT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME_OF_RESTAURANT TEXT,
                        RESTAURANT_PASSWORD TEXT,
                        ADDRESS TEXT,
                        MOBILE_NO INTEGER,
                        RESTAURANT_WALLET_BALANCE INTEGER
                       )''')

    print("Table Created Successfully")
