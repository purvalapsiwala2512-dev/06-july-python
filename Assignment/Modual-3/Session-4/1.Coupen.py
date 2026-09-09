class InvalidCouponCodeError(Exception):
    
    def __init__(self,*args):
        super().__init__(*args)

list = ["ZOMATO50","TASTY20","HUNGRY100"]
coupon = input("Enter coupon code:")
try:
    if coupon not in list:
        raise InvalidCouponCodeError(coupon)
    else:
        print("Valid Code")
except InvalidCouponCodeError as e:
    print(e,"Code is not Valid!!")