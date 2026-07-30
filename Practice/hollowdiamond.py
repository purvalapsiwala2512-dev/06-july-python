lines = 5  # You can adjust this to any height

# Top half (including middle row)
for i in range(lines):
    for k in range((lines - 1) - i):
        print(" ", end="")
    for j in range(i + 1):
        # Print star only at the boundaries (first and last column of the row)
        if j == 0 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# Bottom half
for i in range(lines - 1):
    for k in range(i + 1):
        print(" ", end="")
    for j in range((lines - 1) - i):
        # Print star only at the boundaries
        if j == 0 or j == (lines - 2) - i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()