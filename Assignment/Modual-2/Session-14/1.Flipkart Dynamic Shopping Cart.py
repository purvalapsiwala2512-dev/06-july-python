import json

cart = {}

cart["rahul_k"] = {
    "item_101": {"name": "Wireless Headphones", "quantity": 1, "price": 2999},
    "item_102": {"name": "Running Shoes", "quantity": 1, "price": 1499}
}

cart["priya_m"] = {
    "item_201": {"name": "Leather Wallet", "quantity": 2, "price": 799},
    "item_202": {"name": "Analog Watch", "quantity": 1, "price": 3499}
}

print(json.dumps(cart, indent=4))