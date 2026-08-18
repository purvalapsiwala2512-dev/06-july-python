names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

premium_products = [(name, price) for name, price in zip(names, prices) if price > 1000]

print(premium_products)