lines=5

# for i in range(lines):
#     for j in range(lines):
#         print("*",end="")
#     print()


# for i in range(lines):
#     for j in range(i+1):
#         print("*",end="")
#     print()


for i in range(lines):
    for j in range(lines-i):
        print("*",end="")
    print()


# for i in range(lines):
#     for k in range((lines-1)-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()



# for i in range(lines):
#     for k in range((lines-1)-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()


# for i in range(lines):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(lines-i):
#         if k==0 or k==lines-i-1 or i==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# for i in range(lines):
#     for k in range(i):
#             print(" ",end="")
#     for j in range(lines-i):
#         print("*",end="")
#     print()


# for i in range(lines):
#     for k in range(i):
#             print(" ",end="")
#     for j in range(lines-i):
#         print("* ",end="")
#     print()



# for i in range(lines-1):
#     for k in range(lines-i):
#             print(" ",end="")
#     for j in range(i+1):
#         if j==0 or j==i:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(lines):
#     for k in range(1+i):
#             print(" ",end="")
#     for j in range(lines-i):
#         if j==0 or j==lines-(i+1):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()



# for i in range(lines-1):
#     for k in range((lines-1)-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()
# for i in range(lines):
#     for k in range(i):
#             print(" ",end="")
#     for j in range(lines-i):
#         print("* ",end="")
#     print()


# for i in range(lines):
#     for j in range(lines-i):
#         print(i+1,end="")
#     print()    