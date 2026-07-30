lines = 3  

for i in range(lines):
    for k in range((lines - 1) - i):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()


for i in range(lines - 1):
    for k in range(i + 1):
        print(" ", end="")
    for j in range((lines - 1) - i):
        print("* ", end="")
    print()