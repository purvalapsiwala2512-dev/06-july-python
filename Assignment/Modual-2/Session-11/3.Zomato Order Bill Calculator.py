import math

def calculate_final_bill(bill_amount):
    discounted_bill = bill_amount * 0.90
    final_bill = math.floor(discounted_bill)
    return final_bill

bill_total = 455.80
print(f"Original Bill: ₹{bill_total}")
print(f"Final Payable Amount: ₹{calculate_final_bill(bill_total)}")