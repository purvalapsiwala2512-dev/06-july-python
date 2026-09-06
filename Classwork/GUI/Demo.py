from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Myapp")

# b = Button(root,text="Submit")
# b.pack(side=LEFT)
# b1= Button(root,text="Submit")
# b1.pack(side=RIGHT)
# b2 = Button(root,text="Submit")
# b2.pack(side=TOP)
# b3 = Button(root,text="Submit")
# b3.pack(side=BOTTOM)


l1 = Label(root, text="Username")
l1.grid(row=1,column=1)

l2 = Label(root, text="Email")
l2.grid(row=2,column=1)

l3 = Label(root, text="Phone")
l3.grid(row=3,column=1)


t1 = Entry(root)
t1.grid(row=1,column=2)
t2 = Entry(root)
t2.grid(row=2,column=2)
t3 = Entry(root)
t3.grid(row=3,column=2)

b = Button(root, text="submit")
b.grid(row=4,column=2)

root.mainloop()
