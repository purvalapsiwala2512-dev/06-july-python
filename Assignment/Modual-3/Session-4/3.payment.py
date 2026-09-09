class PaymentFailedError(Exception):
    pass

amount = int(input("Enter Amount:"))
def process_payment(amount):
    try:
        if amount<=0:
            raise PaymentFailedError(amount)
        else:
            print("Payment Successful")
    except PaymentFailedError as s:
        print("Invalid amount",s)

process_payment(amount)