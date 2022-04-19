keyid = 'rzp_test_x9eUElDCdW7AEq'
keySecret = 'fnABDwanQymuuxgaTa8tF7nK'

import razorpay
client = razorpay.Client(auth=(keyid,keySecret))

data = {
    'amount' : 100*100,
    "currency" : "INR",
    "receipt" : "Foodex",
    "notes" :{
        "name" : "Akash",
        "payment_for" : "Food Order"
    }
}

order = client.order.create(data=data)
print(order)