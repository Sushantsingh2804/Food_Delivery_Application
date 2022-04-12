from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'DELIVERYBOY'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE DELIVERYBOY(
                        DELIVERYBOY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME_OF_DELIVERYBOY TEXT,
                        DELIVERYBOY_PASSWORD TEXT,
                        ADDRESS TEXT,
                        DELIVERYBOY_STATUS TEXT,
                        DELIVERYBOY_PHONE_NO INTEGER,
                        DELIVERYBOY_WALLET_BALANCE INTEGER
                       )''')

    print("Table Created Successfully")