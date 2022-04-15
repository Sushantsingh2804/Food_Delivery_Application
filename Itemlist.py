from flask import Flask, request, render_template, flash
import sqlite3 as s

from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
table1 = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='ITEMLIST'").fetchall()

if table1 != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE ITEMLIST(
                        ITEMLIST_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ORDER_ID INTEGER FOREIGN KEY REFERENCE ORDER(ORDER_ID),
                        ITEM_ID INTEGER FOREIGN KEY REFERENCE MENU(ITEM_ID)
                       )''')
    print("Table Created Successfully")

itemlist=Flask(__name__)

@itemlist.route("/dashboard6",methods = ["GET","POST"])
def adding_itemlist():
    if request.method == "POST":
        getid=request.form["ITEM_ID"]
        getid2=request.form["ORDER_ID"]
        print(getid)
        print(getid2)
        try:
            connection.execute("insert into ITEMLIST(ITEM_ID,ORDER_ID)\
                               values('" + getid + "','" + getid2 + "')")
            connection.commit()
            print("Itemlist Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard6.html")

@itemlist.route("/viewall6")
def view_itemlist():
    cursor=connection.cursor()
    count=cursor.execute("select * from ITEMLIST")
    result=cursor.fetchall()
    return render_template("viewall6.html",ITEMLIST=result)

@itemlist.route("/search6",methods = ["GET","POST"])
def search_itemlist():
    if request.method == "POST":
        getid=request.form["ITEM_ID"]
        print(getid)
        cursor = connection.cursor()
        count = cursor.execute("select * from ITEMLIST where ITEM_ID="+getid)
        result = cursor.fetchall()
        return render_template("search6.html", searchitemlist=result)

    return render_template("search6.html")

@itemlist.route("/delete6",methods = ["GET","POST"])
def delete_itemlist():
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        print(getid)
        try:
            connection.execute("delete from ITEMLIST where ITEM_ID="+getid)
            connection.commit()
            print("Itemlist Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete6.html")

@itemlist.route('/up6', methods=['GET', 'POST'])
def updation():
    cursor = connection.cursor()
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        count = cursor.execute("SELECT * FROM ITEMLIST WHERE ITEM_ID='" + getid + "'")
        result = cursor.fetchall()
        if result is None:
            print("Itemlist Not Exist")
        else:
            return render_template("up6.html", search=result, status=True)
    else:
        return render_template("up6.html", search=[], status=False)

@itemlist.route("/update6",methods = ["GET","POST"])
def update_cart():
    if request.method == "POST":
        getid = request.form["ITEM_ID"]
        getid2 = request.form["ORDER_ID"]
        try:
            connection.execute("update ITEMLIST set ITEM_ID="+getid2+" where ORDER_ID="+getid+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update6.html")


if __name__=="__main__":
    itemlist.run()