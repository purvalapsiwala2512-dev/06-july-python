f = open("orders.txt","w")
s = ["Order-1: \n","Order-2:\n","Order-3: \n","Order-4: \n","Order-5: \n","Order-6: \n","Order-7: \n"]
f.writelines(s)
f.close()


f = open("orders.txt")
while True:
    data = f.readline()
    if data == "":
        break
    print(data,end="")
    print(f.tell(),"\n")
f.close()