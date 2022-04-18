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
                        USER_WALLET_BALANCE INTEGER
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

################################# cart table ###############################################

table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='CART'").fetchall()

if table != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE CART(
                        USER_ID INTEGER, 
  						ITEM_ID INTEGER,
  						RESTAURANT_ID INTEGER,
                        FOREIGN KEY(RESTAURANT_ID) REFERENCES RESTAURANT(RESTAURANT_ID)
  						FOREIGN KEY(USER_ID) REFERENCES USER(USER_ID),
                        FOREIGN KEY(ITEM_ID) REFERENCES MENU(ITEM_ID)
                       )''')
    print("Table Created Successfully")
#################################### order table ############################################
table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='ORDER_TABLE'").fetchall()

if table != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE ORDER_TABLE(
                        ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ORDER_AMOUNT INTEGER,
                        DELIVERYBOY_ID INTEGER, 
                        ORDER_STATUS TEXT,  						
                        USER_ID INTEGER, 
  						RESTAURANT_ID INTEGER, 
  						FOREIGN KEY (USER_ID) REFERENCES USER(USER_ID),
  						FOREIGN KEY (DELIVERYBOY_ID) REFERENCES DELIVERYBOY(DELIVERYBOY_ID),
  						FOREIGN KEY (RESTAURANT_ID) REFERENCES RESTAURANT(RESTAURANT_ID)             
                       )''')
    print("Table Created Successfully")
###################################### ITEM LIST ####################################
table = connection.execute("SELECT NAME FROM sqlite_master WHERE type='table' AND name='ITEM_LIST'").fetchall()

if table != []:
    print("Table Already Exist")
else:
    connection.execute('''CREATE TABLE ITEM_LIST(
                        ORDER_ID INTEGER,                        
                        ITEM_ID INTEGER,
                        Item_count INTEGER,
                        FOREIGN KEY (ORDER_ID) REFERENCES ORDER_TABLE(ORDER_ID),
                        FOREIGN KEY (ITEM_ID) REFERENCES MENU(ITEM_ID)
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
    cursor.execute("SELECT m.ITEM_ID,m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m LEFT JOIN RESTAURANT r ON m.RESTAURANT_ID = r.RESTAURANT_ID WHERE m.RESTAURANT_ID="+str(session["id"])+"; ")
    result=cursor.fetchall()
    return render_template("View_Menu.html",MENU=result)
@app.route("/Delete-Item")
def Delete_Item():
    getid = request.args.get('id')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM MENU where ITEM_ID=" + getid)
    result = cursor.fetchall()
    connection.execute("delete from MENU where ITEM_ID=" + getid)
    connection.commit()
    print("Menu data Deleted Successfully.")
    return render_template("Resturant_Delete_item.html", Item=result)

@app.route("/Edit-Item")
def Edit_Item():
    getid = str(request.args.get('id'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM MENU where ITEM_ID=" + getid)
    result = cursor.fetchall()
    return render_template("Update_Menu_Item.html", Item=result)

@app.route("/Update-Item",methods = ["GET","POST"])
def Update_Item():
    if request.method == "POST":
        try:
            getid = request.form["ITEM_ID"]
            print(getid)
            getname = request.form["ITEM_NAME"]
            print(getname)
            getcategory = request.form["ITEM_CATEGORY"]
            print(getcategory)
            getprice = request.form["ITEM_PRICE"]
            print(getprice)
            connection.execute("UPDATE MENU SET ITEM_NAME=" +getname+ ",ITEM_CATEGORY=" +getcategory+ ",ITEM_PRICE=" +getprice+ " WHERE ITEM_ID= " +getid )
            return redirect("/View-Menu")
        except Exception as e:
            print("Error occured ", e)
    return render_template("Update_Menu_Item.html")
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
                getname = i[1]
                getemail = i[3]
                getid = i[0]
                session["name"] = getname
                session["id"] = getid
                session["email"] = getemail
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
        setwallet = '1000'
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
    count=cursor.execute("SELECT m.ITEM_ID,m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m LEFT JOIN RESTAURANT r ON m.RESTAURANT_ID = r.RESTAURANT_ID WHERE m.RESTAURANT_ID="+str(getid)+"; ")
    result=cursor.fetchall()
    return render_template("View_Menu_user.html",MENU=result,Res_id=getid)

@app.route("/User-cart")
def view_cart():
    cursor=connection.cursor()
    cursor.execute("SELECT m.ITEM_ID,m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE,COUNT(m.ITEM_ID) FROM MENU m LEFT JOIN CART c ON m.ITEM_ID = c.ITEM_ID WHERE c.USER_ID="+str(session["id"])+" GROUP BY m.ITEM_ID; ")
    result=cursor.fetchall()
    return render_template("User_Cart.html",Items=result)

@app.route("/User-add-cart")
def add_cart():
    getid= request.args.get('res_id')
    getid_i = request.args.get('id')
    getid_u = str(session["id"])
    connection.execute("insert into CART(ITEM_ID,USER_ID,RESTAURANT_ID)values('" + getid_i + "','" + getid_u + "','" + getid + "')")
    connection.commit()
    print("Added to Successfully.")
    cursor = connection.cursor()
    cursor.execute("SELECT m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m WHERE m.ITEM_ID = "+str(getid_i)+"; ")
    result = cursor.fetchall()
    return render_template("User_Add_Item.html", Item=result ,id = getid)

@app.route("/RemoveFrom-Cart")
def remove_cart():
    getid= request.args.get('id')
    connection.execute("delete from CART where ITEM_ID="+getid)
    connection.commit()
    print("Deleted to Successfully.")
    cursor = connection.cursor()
    cursor.execute("SELECT m.ITEM_NAME,m.ITEM_CATEGORY,m.ITEM_PRICE FROM MENU m WHERE m.ITEM_ID = "+str(getid)+"; ")
    result = cursor.fetchall()
    return render_template("User_Delete_Item.html", Item=result)

@app.route("/Place-Order")
def place_order():
    getid = str(session["id"])
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(m.item_price),c.RESTAURANT_ID FROM CART c JOIN MENU m on m.ITEM_ID=c.ITEM_ID WHERE c.USER_ID="+getid)
    result = cursor.fetchall()
    print(result[0][0])
    if result[0][0] is not None:
        for i in result:
            connection.execute("Insert into ORDER_TABLE(ORDER_AMOUNT,ORDER_STATUS,USER_ID,RESTAURANT_ID) values("+str(i[0])+",'Order Placed'," +getid+ ","+str(i[1])+")")
            connection.commit()
    cursor.execute("SELECT O.order_id,C.item_id,COUNT(C.item_id) FROM CART C JOIN ORDER_TABLE O ON C.USER_ID=O.USER_ID WHERE C.user_id="+getid)
    result = cursor.fetchall()
    print(result)
    if result[0][0] is not None:
        for i in result:
            connection.execute('Insert into ITEM_LIST(ORDER_ID,ITEM_ID,Item_count) values('+str(i[0])+','+str(i[1])+','+str(i[2])+')')
            connection.commit()
    print("Order Added Successfully.")
    connection.execute("delete from CART where USER_ID=" + getid)
    connection.commit()
    print("Cart Empty now")
    cursor.execute("SELECT SUM(ORDER_AMOUNT) FROM ORDER_TABLE WHERE USER_ID=" + getid +" AND ORDER_STATUS='Order Placed'")
    order_ammount = cursor.fetchall()[0][0]
    if order_ammount is not None:
        cursor.execute("SELECT USER_WALLET_BALANCE FROM USER WHERE USER_ID=" + getid)
        User_Wallet = cursor.fetchall()[0][0]
        User_Balance = User_Wallet-order_ammount
        connection.execute("update USER set USER_WALLET_BALANCE='" + str(User_Balance) + "' where USER_ID=" + getid)
        connection.execute("update ORDER_TABLE SET ORDER_STATUS= 'Ammount Paid' WHERE USER_ID=" + getid)
        connection.commit()

    cursor.execute("SELECT order_id, order_amount, order_status,r.name_of_restaurant FROM ORDER_TABLE o JOIN RESTAURANT r on o.RESTAURANT_ID=r.RESTAURANT_ID WHERE o.USER_ID= " + getid)
    result = cursor.fetchall()
    return render_template("User_Order.html", Items=result)
@app.route("/User-order")
def view_Order():
    getid = str(session["id"])
    cursor=connection.cursor()
    cursor.execute("SELECT order_id, order_amount, order_status,r.name_of_restaurant FROM ORDER_TABLE o JOIN RESTAURANT r on o.RESTAURANT_ID=r.RESTAURANT_ID WHERE o.USER_ID= "+getid)
    result=cursor.fetchall()
    return render_template("User_Order.html",Items=result)

@app.route("/View-Order-Detail")
def View_Order_Detail():
    getid_o = request.args.get('id')
    getid_u = str(session["id"])
    cursor = connection.cursor()
    cursor.execute("SELECT order_id, order_amount, order_status,r.name_of_restaurant FROM ORDER_TABLE o JOIN RESTAURANT r on o.RESTAURANT_ID=r.RESTAURANT_ID WHERE o.USER_ID= " + getid_u)
    result = cursor.fetchall()
    cursor = connection.cursor()
    cursor.execute("SELECT m.item_name,i.item_count FROM ITEM_LIST i JOIN MENU m on i.ITEM_ID=m.ITEM_ID WHERE i.ORDER_ID= "+str(getid_o)+"; ")
    Item_list = cursor.fetchall()
    return render_template("View_Order_Detail.html", Order=result, Item_list = Item_list)

if __name__ == "__main__":
    app.run()