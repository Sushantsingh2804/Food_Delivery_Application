from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'USER'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE RESTAURANT(
                        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USER_NAME TEXT,
                        USER_PASSWORD TEXT,
                        USER_EMAIL TEXT,
                        USER_PHONE_NO INTEGER,
                        USER_ADDRESS TEXT,
                        USER_WALLET_BALANCE
                       )''')

    print("Table Created Successfully")