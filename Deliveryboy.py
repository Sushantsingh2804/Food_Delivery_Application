deliveryboy=Flask(_name_)

@deliveryboy.route("/",methods = ["GET","POST"])
def deliveryboy_login():
    global result1, result2, a, b
    if request.method == "POST":
        getEmail = request.form["email"]
        getPass = request.form["pass"]
        result1 = connection.execute("SELECT EMAIL FROM DELIVERY_BOY")
        result2 = connection.execute("SELECT PASS FROM DELIVERY_BOY")
        for i in result1:
            print(i[0])
            result1 = i[0]
        for j in result2:
            print(j[0])
            result2 = j[0]
        if getEmail == result1 and getPass == result2:
            return redirect('/login')
        else:
            return render_template("deliveryboy_login.html", status=True)
    else:
        return render_template("deliveryboy_login.html", status=False)


@deliveryboy.route("/dashboard",methods = ["GET","POST"])
def deliveryboy_registration():
    if request.method == "POST":
        getname=request.form["NAME_OF_DELIVERYBOY"]
        getpassword=request.form["DELIVERYBOY_PASSWORD"]
        getaddress=request.form["ADDRESS"]
        getstatus=request.form["DELIVERYBOY_STATUS"]
        getphone=request.form["DELIVERYBOY_PHONE_NO"]
        getwallet= request.form["DELIVERYBOY_WALLET_BALANCE"]
        print(getname)
        print(getpassword)
        print(getaddress)
        print(getstatus)
        print(getphone)
        print(getwallet)
        try:
            connection.execute("insert into DELIVERYBOY(NAME_OF_DELIVERYBOY,DELIVERYBOY_PASSWORD,ADDRESS,DELIVERYBOY_STATUS,DELIVERYBOY_PHONE_NO,DELIVERYBOY_WALLET_BALANCE)\
                               values('" + getname + "','" + getpassword + "','" + getaddress + "','" + getstatus + "'," + getphone + "," + getwallet + ")")
            connection.commit()
            print("Delivery Boy Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard.html")

@deliveryboy.route("/viewall")
def view_deliveryboy():
    cursor=connection.cursor()
    count=cursor.execute("select * from DELIVERYBOY")
    result=cursor.fetchall()
    return render_template("viewall.html",DELIVERYBOY=result)

@deliveryboy.route("/search",methods = ["GET","POST"])
def search_deliveryboy():
    if request.method == "POST":
        getphone=request.form["DELIVERYBOY_PHONE_NO"]
        print(getphone)
        cursor = connection.cursor()
        count = cursor.execute("select * from DELIVERYBOY where getphone="+getphone)
        result = cursor.fetchall()
        return render_template("search.html", searchdeliveryboy=result)

    return render_template("search.html")

@deliveryboy.route("/delete",methods = ["GET","POST"])
def delete_deliveryboy():
    if request.method == "POST":
        getphone = request.form["DELIVERYBOY_PHONE_NO"]
        print(getphone)
        try:
            connection.execute("delete from DELIVERYBOY where getphone="+getphone)
            connection.commit()
            print("Delivery Boy data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete.html")

@deliveryboy.route("/update",methods = ["GET","POST"])
def update_deliveryboy():
    if request.method == "POST":
        getname = request.form["NAME_OF_DELIVERYBOY"]
        getpassword = request.form["DELIVERYBOY_PASSWORD"]
        getaddress = request.form["ADDRESS"]
        getstatus = request.form["DELIVERYBOY_STATUS"]
        getphone = request.form["DELIVERYBOY_PHONE_NO"]
        getwallet = request.form["DELIVERYBOY_WALLET_BALANCE"]
        try:
            connection.execute("update DELIVERYBOY set NAME_OF_DELIVERYBOY='"+getname+"',DELIVERYBOY_PASSWORD="+getpassword+",ADDRESS='"+getaddress+"',DELIVERYBOY_STATUS='"+getstatus+"',DELIVERYBOY_WALLET_BALANCE="+getwallet+" where DELIVERYBOY_PHONE_NO='"+getphone+"")
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update.html")


if _name=="main_":
    Deliveryboy.run()