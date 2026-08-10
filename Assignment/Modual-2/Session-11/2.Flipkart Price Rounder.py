import math

prices = [199.1, 349.8, 599.3]
rounded_prices = [math.ceil(price) for price in prices]

print("Original Prices:", prices)
print("Rounded Up Prices (₹):", rounded_prices)