from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='ORDER'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE ORDER(
                        ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ORDER_AMOUNT INTEGER,
                        DELIVERYBOY_STATUS TEXT FOREIGN KEY REFERENCE DELIVERYBOY(DELIVERYBOY_ID),
                        DELIVERYBOY_ID INTEGER FOREIGN KEY REFERENCE DELIVERYBOY(DELIVERYBOY_ID),
                        USER_ID INTEGER FOREIGN KEY REFERENCE USER(USER_ID),
                        RESTAURANT_ID INTEGER FOREIGN KEY REFERENCE RESTAURANT(RESTAURANT_ID)
                       )''')
    print("Table Created Successfully")

order=Flask(__name__)

@order.route("/dashboard5",methods = ["GET","POST"])
def adding_order():
    if request.method == "POST":
        getamount=request.form["ORDER_AMOUNT"]
        getid=request.form["USER_ID"]
        getid2=request.form["RESTAURANT_ID"]
        getid3=request.form["DELIVERYBOY_ID"]
        getstatus=request.form["DELIVERYBOY_STATUS"]
        print(getid)
        print(getid2)
        print(getid3)
        print(getamount)
        print(getstatus)
        try:
            connection.execute("insert into ORDER(ORDER_AMOUNT,USER_ID,RESTAURANT_ID,DELIVERYBOY_ID,DELIVERYBOY_STATUS)\
                               values('" +getamount+ "','" + getid + "','" + getid2 + "','" + getid3 + "'," +getstatus+ ")")
            connection.commit()
            print("Order Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard5.html")

@order.route("/viewall5")
def view_order():
    cursor=connection.cursor()
    count=cursor.execute("select * from ORDER")
    result=cursor.fetchall()
    return render_template("viewall5.html",ORDER=result)

@order.route("/search5",methods = ["GET","POST"])
def search_order():
    if request.method == "POST":
        getid=request.form["USER_ID"]
        print(getid)
        cursor = connection.cursor()
        count = cursor.execute("select * from ORDER where USER_ID="+getid)
        result = cursor.fetchall()
        return render_template("search5.html", searchcart=result)

    return render_template("search5.html")

@order.route("/delete5",methods = ["GET","POST"])
def delete_order():
    if request.method == "POST":
        getid = request.form["USER_ID"]
        print(getid)
        try:
            connection.execute("delete from ORDER where USER_ID="+getid)
            connection.commit()
            print("Order Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete5.html")

@order.route('/up5', methods=['GET', 'POST'])
def updation():
    cursor = connection.cursor()
    if request.method == "POST":
        getid = request.form["USER_ID"]
        count = cursor.execute("SELECT * FROM ORDER WHERE USER_ID='" + getid + "'")
        result = cursor.fetchall()
        if result is None:
            print("Order Not Exist")
        else:
            return render_template("up5.html", search=result, status=True)
    else:
        return render_template("up5.html", search=[], status=False)

@ORDER.route("/update5",methods = ["GET","POST"])
def update_order():
    if request.method == "POST":
        getamount = request.form["ORDER_AMOUNT"]
        getid = request.form["USER_ID"]
        getid2 = request.form["RESTAURANT_ID"]
        getid3 = request.form["DELIVERYBOY_ID"]
        getstatus = request.form["DELIVERYBOY_STATUS"]
        try:
            connection.execute("update ORDER set USER_ID="+getid+" where RESTAURANT_ID="+getid2+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update5.html")


if __name__=="__main__":
    order.run()