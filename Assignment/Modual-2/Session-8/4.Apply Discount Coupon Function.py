def apply_coupon(amount, coupon_code=None):
    if coupon_code == 'SAVE10':
        return amount * 0.90  
    return amount

print("Original Price (no coupon): ₹", apply_coupon(1000))

print("Discounted Price (SAVE10): ₹", apply_coupon(1000, 'SAVE10'))

print("Price with invalid coupon: ₹", apply_coupon(1000, 'EXPIRED'))