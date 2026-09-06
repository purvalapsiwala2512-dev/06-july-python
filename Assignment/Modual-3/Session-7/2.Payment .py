class Payment:

    def pay(self,amount):
        self.amount = amount
        print(f"Paying {amount}")

class UPI(Payment):
    
    def pay(self,amount):
        print(f"Paying{amount}via UPI")

k = Payment()
k.pay(100)

s = UPI()
s.pay(555)