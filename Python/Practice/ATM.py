balance = 0
choice=0
while choice !=4:
    
    choice = int(input("""
                    1.Deposite
                    2.Withdrow
                    3.Balance
                    4.exit
                    """))
    if choice==1:
        print("*****Deposite*****")
        amount = int(input("Enter Amount : "))
        balance+=amount
        print("Done")
    elif choice==2:
        print("*****Withdrow*****")
        amount = int(input("Enter Amount : "))
        if amount>balance:
            print("Insufficent Amount")
        else:
            balance-=amount
            print("Done")
        
    elif choice==3:
        print("*****Check Your Balance*****")
        print("Current balance is : ",balance)
    elif choice==4:
        print("You are exit...")
    else:
        print("Invalid choice")