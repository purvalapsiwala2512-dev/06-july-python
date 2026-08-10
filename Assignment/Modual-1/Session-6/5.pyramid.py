total_rows = 4
row = 1

while row <= total_rows:

    spaces = total_rows - row
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
        
    stars = (2 * row) - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
        
    print()
    row += 1