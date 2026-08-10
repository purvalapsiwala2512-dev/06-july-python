food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}

print(f"Food items: {list(food_order.keys())}")

print(f"Quantities: {list(food_order.values())}")

print("Order details:")
for item, qty in food_order.items():
    print(f"- {item}: {qty}")