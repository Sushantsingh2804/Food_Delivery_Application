import razorpay

@app.route('/')
def create_payment():
    return render_template("pay.html")

@app.route('/pay')
def pay():
    global payment, name
    name = request.form.get ("username")
    client = razorpay.Client(auth=("rzp_test_x9eUElDCdW7AEq","fnABDwanQymuuxgaTa8tF7nK"))
    data = {
    'amount' : 100*100,
    "currency" : "INR",
    "receipt" : "Foodex",
    }
    payment = client.order.create(data=data)
    return render_template("payment.html", payment=payment)