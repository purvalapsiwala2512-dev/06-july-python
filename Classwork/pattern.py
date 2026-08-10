# *****
# *****
# *****
# *****
# *****

# for j in range(7):
#     for i in range(15):
#         print("*",end="")
#     print()

# for j in range(5):
#     print(7*"*")
   
   
# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(5):
#     print((i+1)*"*")
   
# *****
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print()

# for i in range(5):
#     print("*"*(5-i))

#     *
#    **
#   ***
#  ****
# *****
   
# lines=9
# for i in range(lines):
#     for k in range((lines-1)-i):
#             print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# *****
#  ****
#   ***
#    **
#     *

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# lines=9
# for i in range(lines):
#     for k in range((lines-1)-i):
#             print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()

# homework:
      #*
     #* *
    #* * *
     #* *
    #  *
    
           #*
          #* *
         #*   *
          #* *
           #*
    
    
# 1
# 12
# 123
# 1234
# 12345


# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

# 5
# 45
# 345
# 2345
# 12345

# 0
# 10
# 010
# 1010
# 01010

# for i in range(5):
#     for j in range(i+1):
#         print((i+j)%2,end="")
#     print()


# for i in range(5):
#     for j in range(i+1):
#         if i%2==j%2:
#             print("0",end="")
#         else:
#             print("1",end="")
#     print()


# *****
#  ****
#   ***
#    **
#     *

lines = 5
for i in range(lines):
    for j in range(i):
        print(" ",end="")
    for k in range(lines-i):
        if k==0 or k==lines-i-1 or i==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()