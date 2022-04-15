from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='CART'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE CART(
                        CART_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USER_ID INTEGER FOREIGN KEY REFERENCE USER(USER_ID),
                        ITEM_ID INTEGER FOREIGN KEY REFERENCE MENU(ITEM_ID)
                       )''')
    print("Table Created Successfully")

cart=Flask(__name__)

@cart.route("/dashboard4",methods = ["GET","POST"])
def adding_cart():
    if request.method == "POST":
        getid=request.form["ITEM_ID"]
        getid2=request.form["USER_ID"]
        print(getid)
        print(getid2)
        try:
            connection.execute("insert into CART(ITEM_ID,USER_ID)\
                               values('" + getid + "','" + getid2 + "')")
            connection.commit()
            print("Cart Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard4.html")

@cart.route("/viewall4")
def view_cart():
    cursor=connection.cursor()
    count=cursor.execute("select * from CART")
    result=cursor.fetchall()
    return render_template("viewall4.html",MENU=result)

@cart.route("/search4",methods = ["GET","POST"])
def search_cart():
    if request.method == "POST":
        getid=request.form["ITEM_ID"]
        print(getid)
        cursor = connection.cursor()
        count = cursor.execute("select * from CART where ITEM_ID="+getid)
        result = cursor.fetchall()
        return render_template("search4.html", searchcart=result)

    return render_template("search4.html")

@cart.route("/delete4",methods = ["GET","POST"])
def delete_cart():
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        print(getid)
        try:
            connection.execute("delete from CART where ITEM_ID="+getid)
            connection.commit()
            print("Cart data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete4.html")

@cart.route('/up4', methods=['GET', 'POST'])
def updation():
    cursor = connection.cursor()
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        count = cursor.execute("SELECT * FROM CART WHERE ITEM_ID='" + getid + "'")
        result = cursor.fetchall()
        if result is None:
            print("Cart Not Exist")
        else:
            return render_template("up4.html", search=result, status=True)
    else:
        return render_template("up4.html", search=[], status=False)

@cart.route("/update3",methods = ["GET","POST"])
def update_cart():
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        getid2 = request.form["USER_ID"]
        try:
            connection.execute("update CART set USER_ID="+getid2+" where ITEM_ID="+getid+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update4.html")


if __name__=="__main__":
    cart.run()