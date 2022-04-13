from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'USER'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE USER(
                        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USER_NAME TEXT,
                        USER_PASSWORD TEXT,
                        USER_EMAIL TEXT,
                        USER_PHONE_NO INTEGER,
                        USER_ADDRESS TEXT,
                        USER_PINCODE TEXT,
                        USER_WALLET_BALANCE
                       )''')

    print("Table Created Successfully")

user = Flask(__name__)


@user.route("/",methods = ["GET","POST"])
def user_login():
    global result1, result2
    if request.method == "POST":
        getemail = request.form["USER_EMAIL"]
        getpassword = request.form["USER_PASSSWORD"]
        result1 = connection.execute("SELECT USER_EMAIL FROM USER")
        result2 = connection.execute("SELECT USER_PASSWORD FROM USER")
        for i in result1:
            print(i[0])
            result1 = i[0]
        for j in result2:
            print(j[0])
            result2 = j[0]
        if getemail == result1 and getpassword == result2:
            return redirect('/User-Dashboard')
        else:
            return render_template("User_login.html", status=True)
    else:
        return render_template("User_login.html", status=False)


@user.route("/User-Registration", methods=["GET", "POST"])
def user_registration():
    if request.method == "POST":
        getname=request.form["USER_NAME"]
        getemail=request.form["USER_EMAIL"]
        getphone=request.form["USER_PHONE_NO"]
        getpassword=request.form["USER_PASSWORD"]
        getaddress = request.form["ADDRESS"]
        getpincode = request.form["Pincode"]
        setwallet = '0'
        print(getname)
        print(getpassword)
        print(getemail)
        print(getphone)
        print(getaddress)
        print(setwallet)
        try:
            connection.execute("insert into USER(USER_NAME,USER_PASSWORD,USER_EMAIL,USER_PHONE_NO,USER_ADDRESS,USER_PINCODE,USER_WALLET_BALANCE)\
                               values('" + getname + "','" + getpassword + "','" + getemail + "'," + getphone + ",'" + getaddress + "'," + getpincode + "," + setwallet + ")")
            connection.commit()
            print("Restaurant Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)


if __name__=="__main__":
    user.run()