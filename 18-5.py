from tkinter import *

def pr():
    x.set(cd[var.get()])

a = Tk()
a.title("city")
cd = {0:"Tokyo",1:"New York",2:"Paris",3:"London",4:"HongKhong"}

var = IntVar()
var.set(0)
lab = Label(a,text = "Choose the most favoriatable city.",
            width = 30,bg = "red").pack()



for key,val in cd.items():
    Radiobutton(a,text = val,
                variable = var,
                value = key,
                command = pr).pack()
x = StringVar()
lab2 = Label(a,width = 30,bg = "yellow",textvariable = x).pack()

a.mainloop()
