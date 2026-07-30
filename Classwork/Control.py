#control : break, continue, pass

for i in range(10):
    if i==5:
        # break
        continue
    print(i)
    
    
if 10>20:
    print("10 is greate")
else:
    pass



a = int(input("enter number : "))
b = int(input("Enter number : "))
choice = input("""
               Enter Choice :
               +,-,*,/
               """)

match(choice):
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _ : 
        print("Invalid input")