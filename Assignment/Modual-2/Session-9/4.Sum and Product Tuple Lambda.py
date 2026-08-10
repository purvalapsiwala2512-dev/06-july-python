sum_and_product = lambda a, b: (a + b, a * b)

pairs = [(3, 4), (5, 2), (7, 8)]

for a, b in pairs:
    s, p = sum_and_product(a, b)
    print(f"Pair ({a}, {b}) -> Sum: {s}, Product: {p}")