def get_discounted_price(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

test_price = get_discounted_price(500, 10)
print(f"--- Task 1 ---")
print(f"Final discounted price: {test_price}\n")