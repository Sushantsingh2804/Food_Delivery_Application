foodex=Flask(__name__)

@foodex.route("/",methods = ["GET","POST"])
def RESTAURANT_login():
    if request.method == "POST":
        getusername=request.form["username"]
        getpassword=request.form["password"]
        print(getusername)
        print(getpassword)
        if getusername=="restaurant" and getpassword=="12345":
            return redirect("/dashboard")
    return render_template("admin.html")

@foodex.route("/dashboard",methods = ["GET","POST"])
def RESTAURANT_registration():
    if request.method == "POST":
        getname=request.form["name"]
        getpassword=request.form["password"]
        getaddress=request.form["address"]
        getmobileno=request.form["mobileno"]
        getwalletbalance=request.form["walletbalance"]
        print(getname)
        print(getpassword)
        print(getaddress)
        print(getmobileno)
        print(getwalletbalance)


        try:
            connection.execute("insert into RESTAURANT (name,password,mobileno,address,walletbalance)\
                               values('" + getname + "'," + getpassword + "," + getmobileno + ",'" + getaddress + "','" + getwalletbalance + "')")
            connection.commit()
            print(" Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard.html")

@foodex.route("/viewall")
def view_RESTAURANT():
    cursor=connection.cursor()
    count=cursor.execute("select * from RESTAURANT")
    result=cursor.fetchall()
    return render_template("viewall.html",RESTAURANT=result)

@foodex.route("/search",methods = ["GET","POST"])
def search_RESTAURANT():
    if request.method == "POST":
        getmobileno=request.form["mobileno"]
        print(getmobileno)
        cursor = connection.cursor()
        count = cursor.execute("select * from RESTAURANT where mobileno="+getmobileno)
        result = cursor.fetchall()
        return render_template("search.html", searchRESTAURANT=result)

    return render_template("search.html")

@foodex.route("/delete",methods = ["GET","POST"])
def delete_RESTAURANT():
    if request.method == "POST":
        getname = request.form["name"]
        getpassword = request.form["password"]
        getaddress = request.form["address"]
        getmobileno = request.form["mobileno"]
        getwalletbalance = request.form["walletbalance"]
        print(getname)
        print(getpassword)
        print(getaddress)
        print(getmobileno)
        print(getwalletbalance)



        try:
            connection.execute("delete from RESTAURANT where mobileno="+getmobileno+")
            connection.commit()
            print("Restaurant data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete.html")

@foodex.route("/update",methods = ["GET","POST"])
def update_RESTAURANT():
    if request.method == "POST":
        mobileno=request.form["mobileno"]
        name = request.form["name"]
        password = request.form["password"]
        address = request.form["address"]
        walletbalance = request.form["walletbalance"]
        try:
            connection.execute("update Restaurant set name='"+name+"',address='"+address+"',password='"+password+"',walletbalance='"+walletbalance+"' where mobileno="+mobnumber)
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update.html")



@foodex.route("/",methods = ["GET","POST"])
def RESTAURANT_login():
    if request.method == "POST":
        getusername=request.form["username"]
        getpassword=request.form["password"]
        print(getusername)
        print(getpassword)
        if getusername=="RESTAURANT" and getpassword=="12345":
            return redirect("/dashboard")
    return render_template("admin.html")

@foodex.route("/dashboard",methods = ["GET","POST"])
def RESTAURANT_registration():
    if request.method == "POST":
        getname=request.form["name"]
        getmobileno=request.form["mobileno"]
        getpassword=request.form["password"]
        getaddress=request.form["address"]
        getwalletbalance=request.form["walletbalance"]
        print(getname)
        print(getmobileno)
        print(getpassword)
        print(getaddress)
        print(getwalletbalance)

        try:
            connection.execute("insert into RESTAURANT(name,mobileno,address,password,walletbalance)\
                               values('" + getname + "'," + getmobileno + ",'" + getaddress + "','" + getpassword + "'," + getwalletbalance + ")")
            connection.commit()
            print("Restaurant Data Added Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("dashboard.html")

@foodex.route("/viewall")
def view_RESTAURANT():
    cursor=connection.cursor()
    count=cursor.execute("select * from Restaurant")
    result=cursor.fetchall()
    return render_template("viewall.html",Restaurant=result)

@foodex.route("/search",methods = ["GET","POST"])
def search_RESTAURANT():
    if request.method == "POST":
        getmobileno=request.form["mobileno"]
        print(getmobileno)
        cursor = connection.cursor()
        count = cursor.execute("select * from restaurant where mobileno="+getmobileno)
        result = cursor.fetchall()
        return render_template("search.html", searchrestaurant=result)

    return render_template("search.html")

@foodex.route("/delete",methods = ["GET","POST"])
def delete_RESTAURANT():
    if request.method == "POST":
        getname = request.form["name"]
        getmobileno = request.form["mobileno"]
        getpassword = request.form["password"]
        getaddress = request.form["address"]
        getwalletbalance = request.form["walletbalance"]
        print(getname)
        print(getmobileno)
        print(getpassword)
        print(getaddress)
        print(getwalletbalance)


        try:
            connection.execute("delete from Restaurant where mobileno="+getmobileno)
            connection.commit()
            print("Restaurant data Deleted Successfully.")
        except Exception as e:
            print("Error occured ", e)

    return render_template("delete.html")

@foodex.route("/update",methods = ["GET","POST"])
def update_RESTAURANT():
    if request.method == "POST":
        mobnumber=request.form["mobileno"]
        name = request.form["name"]
        password = request.form["password"]
        address = request.form["address"]
        walletbalance = request.form["walletbalance"]
        try:
            connection.execute("update Restaurant set name='"+name+"',password="+password+",address='"+address+"',mobileno='"+mobileno+"',walletbalance="+walletbalance+" where mobileno="+mobnumber)
            connection.commit()
            print("Updated Successfully")
        except Exception as e:
            print(e)

    return render_template("update.html")
if __name__=="__main__":
    Restaurant.run()


