lines=5

# for i in range(lines):
#     for j in range(lines):
#         print("*",end="")
#     print()


# for i in range(lines):
#     for j in range(i+1):
#         print("*",end="")
#     print()


# for i in range(lines):
#     for j in range(lines-i):
#         print("*",end="")
#     print()


# for i in range(lines):
#     for k in range((lines-1)-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()



for i in range(lines):
    for k in range((lines-1)-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()