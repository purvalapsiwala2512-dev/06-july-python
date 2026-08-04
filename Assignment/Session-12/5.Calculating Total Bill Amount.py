from functools import reduce

prices = [120, 80, 150, 60]

# Using reduce() and a lambda function to sum the list
total_bill = reduce(lambda x, y: x + y, prices)

print(f"--- Task 5 ---")
print(f"Item prices: {prices}")
print(f"Total Swiggy bill amount: {total_bill}")