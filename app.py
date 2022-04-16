from flask import Flask, request, render_template, flash ,session
import sqlite3 as sql
from flask_session import Session
from werkzeug.utils import redirect

connection = sql.connect("foodex.db", check_same_thread=False)
table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'RESTAURANT'").fetchall()

################### resturant table ########################
if table != []:
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
############################### user table ##############################################

table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'USER'").fetchall()

if table != []:
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

############################## delivery table ############################################

table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name= 'DELIVERYBOY'").fetchall()

if table != []:
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

############################## menu table ###############################################
table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='MENU'").fetchall()

if table != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE MENU(
                        ITEM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ITEM_NAME TEXT,
                        ITEM_CATEGORY TEXT,
                        ITEM_PRICE INTEGER,
                        RESTAURANT_ID INTEGER,
                        FOREIGN KEY(RESTAURANT_ID) REFERENCES RESTAURANT(RESTAURANT_ID)
                       )''')
    print("Table Created Successfully")

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods = ["GET","POST"])
def app_start():
    return render_template("Index.html")

############################## resturant ##############################################
@app.route("/Restaurant",methods = ["GET","POST"])
def app_login():
    if request.method == "POST":
        getname = request.form["NAME_OF_RESTAURANT"]
        getPass = request.form["RESTAURANT_PASSWORD"]
        cursor = connection.cursor()
        query = "select * from RESTAURANT where NAME_OF_RESTAURANT='" + getname + "' and RESTAURANT_PASSWORD ='" + getPass + "'"
        result = cursor.execute(query).fetchall()
        if len(result) > 0:
            for i in result:
                getname = i[1]
                getid = i[0]
                session["name"] = getname
                session["id"] = getid
            return redirect("/Resturant-Dashboard")
    return render_template("Resturant_Login.html")

@app.route("/Restaurant-Registration", methods= ["GET", "POST"])
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
        return redirect("/Restaurant")
    return render_template("Resturant_Register.html")

@app.route("/Resturant-Dashboard")
def Resturant_Dashboard():
    if not session.get("name"):
        return redirect("/")
    else:
        return render_template("Resturant_Dashboard.html")

@app.route("/Add-Item",methods = ["GET","POST"])
def Add_Item():
    if request.method == "POST":
        getname = request.form["ITEM_NAME"]
        getcategory = request.form["ITEM_CATEGORY"]
        getprice = request.form["ITEM_PRICE"]
        getid=str(session["id"])
        try:
            connection.execute("insert into MENU(ITEM_NAME,ITEM_CATEGORY,ITEM_PRICE,RESTAURANT_ID)\
                                  values('" + getname + "','" + getcategory + "','" + getprice + "'," + getid + ")")
            connection.commit()
            return redirect("/View-Menu")
        except Exception as e:
            print("Error occured ", e)

    return render_template("Add_Menu_Item.html")

@app.route("/View-Menu")
def view_menu():
    cursor=connection.cursor()
    count=cursor.execute("SELECT m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m LEFT JOIN RESTAURANT r ON m.RESTAURANT_ID = r.RESTAURANT_ID WHERE m.RESTAURANT_ID="+str(session["id"])+"; ")
    result=cursor.fetchall()
    return render_template("View_Menu.html",MENU=result)

##################################### delivery #######################################################################

@app.route("/Delivery", methods=["GET", "POST"])
def deliveryboy_login():
    if request.method == "POST":
        getname = request.form["DELIVERYBOY_NAME"]
        getPass = request.form["DELIVERYBOY_PASSWORD"]
        cursor = connection.cursor()
        query = "select * from DELIVERYBOY where NAME_OF_DELIVERYBOY='" + getname + "' and DELIVERYBOY_PASSWORD ='" + getPass + "'"
        result = cursor.execute(query).fetchall()
        if len(result) > 0:
            for i in result:
                getname = i[1]
                getid = i[0]
                session["name"] = getname
                session["id"] = getid
            return redirect("/Delivery-Dashboard")
    return render_template("DeliveryBoy_Login.html")


@app.route("/Delivery-Registration", methods=["GET", "POST"])
def deliveryboy_registration():
    if request.method == "POST":
        try:
            getname = request.form["NAME_OF_DELIVERYBOY"]
            getphone = request.form["DELIVERYBOY_PHONE_NO"]
            getpassword = request.form["DELIVERYBOY_PASSWORD"]
            getaddress = request.form["ADDRESS"]
            setwallet = '0'
            setstatus = 'available'

            connection.execute("insert into DELIVERYBOY(NAME_OF_DELIVERYBOY,DELIVERYBOY_PASSWORD,ADDRESS,DELIVERYBOY_STATUS,DELIVERYBOY_PHONE_NO,DELIVERYBOY_WALLET_BALANCE)\
                               values('" + getname + "','" + getpassword + "','" + getaddress + "','" + setstatus + "'," + getphone + "," + setwallet + ")")
            connection.commit()
            print("Delivery Boy Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

        return redirect("/Delivery")
    return render_template("DeliveryBoy_Register.html")


@app.route("/Delivery-Dashboard")
def deliveryboy_Dashboard():
    return render_template("DeliveryBoy_Dashboard.html")

################################## user #########################################

@app.route("/User",methods = ["GET","POST"])
def user_login():
    if request.method == "POST":
        getname = request.form["USER_EMAIL"]
        getPass = request.form["USER_PASSSWORD"]
        cursor = connection.cursor()
        query = "select * from USER where USER_EMAIL='" + getname + "' and USER_PASSWORD ='" + getPass + "'"
        result = cursor.execute(query).fetchall()
        if len(result) > 0:
            for i in result:
                getname = i[3]
                getid = i[0]
                session["name"] = getname
                session["id"] = getid
            return redirect("/User-Dashboard")
    return render_template("User_login.html")


@app.route("/User-Registration", methods=["GET", "POST"])
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
        return redirect("/User")
    return render_template("User_Registration.html")

@app.route("/User-Dashboard")
def User_Dashboard():
    return render_template("User_Dashboard.html")

@app.route("/View-Resturant")
def User_View_Resturant():
    cursor = connection.cursor()
    count = cursor.execute("select * from RESTAURANT")
    result = cursor.fetchall()
    return render_template("View_Resturant.html", Resturant=result)

@app.route("/View-Resturant-menu")
def view_menu_user():
    getid=request.args.get('id')
    cursor=connection.cursor()
    count=cursor.execute("SELECT m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m LEFT JOIN RESTAURANT r ON m.RESTAURANT_ID = r.RESTAURANT_ID WHERE m.RESTAURANT_ID="+str(getid)+"; ")
    result=cursor.fetchall()
    return render_template("View_Menu_user.html",MENU=result)

@app.route("/User-cart")
def view_menu_user():
    getid=request.args.get('id')
    cursor=connection.cursor()
    count=cursor.execute("SELECT m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m LEFT JOIN RESTAURANT r ON m.RESTAURANT_ID = r.RESTAURANT_ID WHERE m.RESTAURANT_ID="+str(getid)+"; ")
    result=cursor.fetchall()
    return render_template("User_Cart.html",MENU=result)