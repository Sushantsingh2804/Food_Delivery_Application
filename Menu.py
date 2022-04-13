Menu=Flask(_name_)
@menu.route("/dashboard3",methods = ["GET","POST"])
def adding_menu():
    if request.method == "POST":
        getname=request.form["ITEM_NAME"]
        getcategory=request.form["ITEM_CATEGORY"]
        getprice=request.form["ITEM_PRICE"]
        getid=request.form["RESTAURANT_ID"]
        print(getname)
        print(getcategory)
        print(getprice)
        print(getid)
        try:
            connection.execute("insert into USER(ITEM_NAME,ITEM_CATEGORY,ITEM_PRICE,RESTAURANT_ID)\
                               values('" + getname + "','" + getcategory + "','" + getprice + "'," + getid + ")")
            connection.commit()
            print("Menu Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard3.html")

@user.route("/viewall3")
def view_menu():
    cursor=connection.cursor()
    count=cursor.execute("select * from MENU")
    result=cursor.fetchall()
    return render_template("viewall3.html",MENU=result)

@user.route("/search3",methods = ["GET","POST"])
def search_menu():
    if request.method == "POST":
        getname=request.form["ITEM_NAME"]
        print(getname)
        cursor = connection.cursor()
        count = cursor.execute("select * from MENU where ITEM_NAME="+getname)
        result = cursor.fetchall()
        return render_template("search3.html", searchuser=result)

    return render_template("search3.html")

@user.route("/delete3",methods = ["GET","POST"])
def delete_user():
    if request.method == "POST":
        getname = request.form["ITEM_NAME"]
        print(getname)
        try:
            connection.execute("delete from MENU where ITEM_NAME="+getname)
            connection.commit()
            print("Menu data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete3.html")

@user.route('/up3', methods=['GET', 'POST'])
def updation():
    cursor = connection.cursor()
    if request.method == "POST":
        getname = request.form["ITEM_NAME"]
        count = cursor.execute("SELECT * FROM MENU WHERE ITEM_NAME='" + getname + "'")
        result = cursor.fetchall()
        if result is None:
            print("Menu Not Exist")
        else:
            return render_template("up3.html", search=result, status=True)
    else:
        return render_template("up3.html", search=[], status=False)

@user.route("/update3",methods = ["GET","POST"])
def update_menu():
    if request.method == "POST":
        getname = request.form["ITEM_NAME"]
        getcategory = request.form["ITEM_CATEGORY"]
        getprice = request.form["ITEM_PRICE"]
        getid = request.form["RESTAURANT_ID"]
        try:
            connection.execute("update MENU set ITEM_NAME='"+getname+"',ITEM_CATEGORY="+getcategory+",ITEM_PRICE='"+getprice+"' where RESTAURANT_ID="+getid+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update3.html")


if _name=="main_":
    menu.run()