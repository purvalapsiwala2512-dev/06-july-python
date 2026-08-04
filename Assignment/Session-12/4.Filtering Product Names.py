products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

m_products = list(filter(lambda item: item.startswith('M'), products))

print(f"--- Task 4 ---")
print(f"Original list: {products}")
print(f"Filtered list ('M' products): {m_products}\n")