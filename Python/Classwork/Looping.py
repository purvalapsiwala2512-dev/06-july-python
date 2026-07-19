#Looping : for, while
for i in range(10):
        print(i)

for i in range(5,10):
            print(i)

for i in range(1,10,2):
        print(i)

for i in range(10,1,-1):
        print(i)


i=10
while i<=20:
        print(i)
        i+=1


flag = 'y'
while flag=='y':
    choice  = int(input("enter choice : "))

    match(choice):
        case 1 : print("Gujarati")
        case 2 : print("Hindi")
        case 3 : print("english")
        case _ : print("Invalid choice")
    
    flag = input("Do you want to continue ? press y or n :")
    if flag=='n':
        print("you are exit !!!")