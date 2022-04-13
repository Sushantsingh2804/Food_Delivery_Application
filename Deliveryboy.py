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
                        DELIVERYBOY_EMAIL TEXT,
                        DELIVERYBOY_PHONE_NO INTEGER,
                        DELIVERYBOY_WALLET_BALANCE INTEGER
                       )''')

    print("Table Created Successfully")

deliveryboy=Flask(__name__)

@deliveryboy.route("/2",methods = ["GET","POST"])
def deliveryboy_login():
    global result1, result2, a, b
    if request.method == "POST":
        getemail = request.form["DELIVERYBOY_EMAIL"]
        getpassword = request.form["DELIVERYBOY_PASSWORD"]
        result1 = connection.execute("SELECT EMAIL FROM DELIVERY_BOY")
        result2 = connection.execute("SELECT PASS FROM DELIVERY_BOY")
        for i in result1:
            print(i[0])
            result1 = i[0]
        for j in result2:
            print(j[0])
            result2 = j[0]
        if getEmail == result1 and getPass == result2:
            return redirect('/login2')
        else:
            return render_template("deliveryboy_login.html", status=True)
    else:
        return render_template("deliveryboy_login.html", status=False)


@deliveryboy.route("/dashboard2",methods = ["GET","POST"])
def deliveryboy_registration():
    if request.method == "POST":
        getname=request.form["NAME_OF_DELIVERYBOY"]
        getpassword=request.form["DELIVERYBOY_PASSWORD"]
        getaddress=request.form["ADDRESS"]
        getstatus=request.form["DELIVERYBOY_STATUS"]
        getemail=request.form["DELIVERYBOY_EMAIL"]
        getphone=request.form["DELIVERYBOY_PHONE_NO"]
        getwallet= request.form["DELIVERYBOY_WALLET_BALANCE"]
        print(getname)
        print(getpassword)
        print(getaddress)
        print(getstatus)
        print(getemail)
        print(getphone)
        print(getwallet)
        try:
            connection.execute("insert into DELIVERYBOY(NAME_OF_DELIVERYBOY,DELIVERYBOY_PASSWORD,ADDRESS,DELIVERYBOY_STATUS,DELIVERYBOY_EMAIL,DELIVERYBOY_PHONE_NO,DELIVERYBOY_WALLET_BALANCE)\
                               values('" + getname + "','" + getpassword + "','" + getaddress + "','" + getstatus + "','" + getemail + "'," + getphone + "," + getwallet + ")")
            connection.commit()
            print("Delivery Boy Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard2.html")

@deliveryboy.route("/viewall2")
def view_deliveryboy():
    cursor=connection.cursor()
    count=cursor.execute("select * from DELIVERYBOY")
    result=cursor.fetchall()
    return render_template("viewall2.html",DELIVERYBOY=result)

@deliveryboy.route("/search2",methods = ["GET","POST"])
def search_deliveryboy():
    if request.method == "POST":
        getphone=request.form["DELIVERYBOY_PHONE_NO"]
        print(getphone)
        cursor = connection.cursor()
        count = cursor.execute("select * from DELIVERYBOY where DELIVERYBOY_PHONE_NO="+getphone)
        result = cursor.fetchall()
        return render_template("search2.html", searchdeliveryboy=result)

    return render_template("search2.html")

@deliveryboy.route("/delete2",methods = ["GET","POST"])
def delete_deliveryboy():
    if request.method == "POST":
        getphone = request.form["DELIVERYBOY_PHONE_NO"]
        print(getphone)
        try:
            connection.execute("delete from DELIVERYBOY where DELIVERYBOY_PHONE_NO="+getphone)
            connection.commit()
            print("Delivery Boy data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete2.html")

@restaurant.route('/up2', methods=['GET', 'POST'])
def updation():
    global getname
    cursor = connection.cursor()
    if request.method == "POST":
        getname = request.form["NAME_OF_DELIVERYBOY"]
        count = cursor.execute("SELECT * FROM DELIVERYBBOY WHERE NAME_OF_DELIVERYBOY='" + getname + "'")
        result = cursor.fetchall()
        if result is None:
            print("Delivery boy Name Not Exist")
        else:
            return render_template("up2.html", search=result, status=True)
    else:
        return render_template("up2.html", search=[], status=False)

@deliveryboy.route("/update2",methods = ["GET","POST"])
def update_deliveryboy():
    if request.method == "POST":
        getname = request.form["NAME_OF_DELIVERYBOY"]
        getpassword = request.form["DELIVERYBOY_PASSWORD"]
        getaddress = request.form["ADDRESS"]
        getstatus = request.form["DELIVERYBOY_STATUS"]
        getemail = request.form["DELIVERYBOY_EMAIL"]
        getphone = request.form["DELIVERYBOY_PHONE_NO"]
        getwallet = request.form["DELIVERYBOY_WALLET_BALANCE"]
        try:
            connection.execute("update DELIVERYBOY set NAME_OF_DELIVERYBOY='"+getname+"',DELIVERYBOY_PASSWORD="+getpassword+",ADDRESS='"+getaddress+"',DELIVERYBOY_STATUS='"+getstatus+"',DELIVERYBOY_EMAIL='"+getemail+"',DELIVERYBOY_WALLET_BALANCE="+getwallet+" where DELIVERYBOY_PHONE_NO='"+getphone+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update2.html")


if __name__=="__main__":
    deliveryboy.run()