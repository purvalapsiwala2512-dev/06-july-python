prices = [120, 250, 99, 180, 310]

updated_prices = list(map(lambda price: round(price * 1.10, 2), prices))

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)