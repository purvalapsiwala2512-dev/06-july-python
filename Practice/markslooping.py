flag = 'y'
while flag=='y':
    marks = int(input("Enter marks : "))
    if marks>=91 and marks<=100:
        print("Grade A")
    elif marks>=71 and marks<=90:
        print("Grade B")
    elif marks>=51 and marks<=70:
        print("grade C")
    elif marks>=35 and marks<=50:
        print("grade D")
    elif marks>=0 and marks<=34:
        print("grade F")
    else:
        print("Invalid marks")

    flag = input("Do you want to continue ? press y or n :")
    if flag =="n":
         print("you are exit |||")