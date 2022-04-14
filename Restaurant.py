from flask import Flask, request, render_template, flash
import sqlite3 as s
from werkzeug.utils import redirect

connection = s.connect("foodex.db", check_same_thread=False)
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
                        RESTAURANT_PIN TEXT,
                        RESTAURANT_WALLET_BALANCE INTEGER
                       )''')

    print("Table Created Successfully")

restaurant = Flask(__name__)

@restaurant.route("/",methods = ["GET","POST"])
def restaurant_login():
    global result1, result2
    if request.method == "POST":
        getname = request.form["NAME_OF_RESTAURANT"]
        getPass = request.form["RESTAURANT_PASSWORD"]
        result1 = connection.execute("SELECT NAME_OF_RESTAURANT FROM RESTAURANT")
        result2 = connection.execute("SELECT RESTAURANT_PASSWORD FROM RESTAURANT")
        for i in result1:
            print(i[0])
            result1 = i[0]
        for j in result2:
            print(j[0])
            result2 = j[0]
        if getname == result1 and getPass == result2:
            return redirect('/Resturant-Dashboard')
        else:
            return render_template("Resturant_Login.html", status=True)
    else:
        return render_template("Resturant_Login.html", status=False)


@restaurant.route("/Restaurant-Registration", methods= ["GET", "POST"])
def restaurant_registration():
    if request.method == "POST":
        getname = request.form["NAME_OF_RESTAURANT"]
        getphone = request.form["MOBILE_NO"]
        getpassword = request.form["RESTAURANT_PASSWORD"]
        getaddress = request.form["ADDRESS"]
        getpincode= request.form["Pincode"]
        setwallet = '0'
        print(getname)
        print(getpassword)
        print(getaddress)
        print(getphone)
        print(setwallet)
        try:
            connection.execute("insert into RESTAURANT(NAME_OF_RESTAURANT,RESTAURANT_PASSWORD,ADDRESS,MOBILE_NO,RESTAURANT_PIN,RESTAURANT_WALLET_BALANCE)\
                               values('" + getname + "','" + getpassword + "','" + getaddress + "'," + getphone + "," + getpincode + "," + setwallet + ")")
            connection.commit()
            print("Restaurant Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)
        return redirect("/")
    return render_template("Resturant_Register.html")

@restaurant.route("/Resturant-Dashboard")
def deliveryboy_Dashboard():
    return render_template("Resturant_Dashboard.html")

# @restaurant.route("/viewall")
# def view_restaurant():
#     cursor=connection.cursor()
#     count=cursor.execute("select * from RESTAURANT")
#     result=cursor.fetchall()
#     return render_template("viewall.html",RESTAURANT=result)
#
# @restaurant.route("/search",methods = ["GET","POST"])
# def search_restaurant():
#     if request.method == "POST":
#         getphone=request.form["MOBILE_NO"]
#         print(getphone)
#         cursor = connection.cursor()
#         count = cursor.execute("select * from RESTAURANT where MOBILE_NO="+getphone)
#         result = cursor.fetchall()
#         return render_template("search.html", searchdeliveryboy=result)
#
#     return render_template("search.html")
#
# @restaurant.route("/delete",methods = ["GET","POST"])
# def delete_restaurant():
#     if request.method == "POST":
#         getphone = request.form["MOBILE_NO"]
#         print(getphone)
#         try:
#             connection.execute("delete from RESTAURANT where MOBILE_NO="+getphone)
#             connection.commit()
#             print("Restaurant data Deleted Successfully.")
#         except Exception as e:
#             print("Error occured ", e)
#
#     return render_template("delete.html")
#
# @restaurant.route('/up', methods=['GET', 'POST'])
# def updation():
#     global getname
#     cursor = connection.cursor()
#     if request.method == "POST":
#         getname = request.form["NAME_OF_RESTAURANT"]
#         count = cursor.execute("SELECT * FROM RESTAURANT WHERE NAME_OF_RESTAURANT='" + getname + "'")
#         result = cursor.fetchall()
#         if result is None:
#             print("Restaurant Name Not Exist")
#         else:
#             return render_template("up.html", search=result, status=True)
#     else:
#         return render_template("up.html", search=[], status=False)
#
# @restaurant.route("/update",methods = ["GET","POST"])
# def update_restaurant():
#     if request.method == "POST":
#         getname = request.form["NAME_OF_RESTAURANT"]
#         getpassword = request.form["RESTAURANT_PASSWORD"]
#         getaddress = request.form["ADDRESS"]
#         getphone = request.form["MOBILE_NO"]
#         getwallet = request.form["RESTAURANT_WALLET_BALANCE"]
#         try:
#             connection.execute("update RESTAURANT set NAME_OF_RESTAURANT='"+getname+"',RESTAURANT_PASSWORD="+getpassword+",ADDRESS='"+getaddress+"',RESTAURANT_WALLET_BALANCE="+getwallet+" where MOBILE_NO='"+getphone+"")
#             connection.commit()
#             print("Updated Successfully")
#         except Exception as e:
#             print(e)
#
#     return render_template("update.html")
#

if __name__=="__main__":
    restaurant.run()