zomato_orders = {}

def add_order(orders, order_id, restaurant, items, total):
    """Adds a new order to the orders dictionary."""
    orders[order_id] = {
        'restaurant': restaurant,
        'items': items,
        'total': total
    }

def update_order_total(orders, order_id, new_total):
    """Updates the total for an existing order or initializes a default if missing."""
    order = orders.setdefault(order_id, {'restaurant': 'Unknown', 'items': [], 'total': 0})
    order['total'] = new_total

add_order(zomato_orders, 1001, "Meghana Foods", ["Biryani", "Coke"], 450)
print("Initial Order:", zomato_orders)

update_order_total(zomato_orders, 1001, 500)
print("Updated Order:", zomato_orders)