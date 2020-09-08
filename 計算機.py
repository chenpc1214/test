from tkinter import *

a = Tk()
a.title("test")
a.geometry = ("500x500")

x = StringVar()
x.set("0")

def cal():
    result = eval(x.get())
    x.set(x.get() + " = \n"+ str(result) )

def show(sth):
    content = x.get()
    if content == "0":
        content = ""
    x.set(content + sth)

def backspace():
    x.set(str(x.get()[:-1]))

def clear():
    x.set("0")

lab = Label(a,width = 25, height = 2,relief = "raised",anchor = SE,textvariable = x)
lab.grid(row = 0,column = 0,columnspan = 4,padx = 5, pady= 5)
    
cb = Button(a,text = "C",width = 5,command = clear)
deln = Button(a,text = "DEL",width = 5,command = backspace)
div = Button(a,text = "%",width = 5,command = lambda:show("%"))
div2 = Button(a,text = "/",width = 5,command = lambda:show("/"))

seven = Button(a,text = "7",width = 5,command = lambda:show("7"))
nine = Button(a,text = "9",width = 5,command = lambda:show("9"))
eight = Button(a,text = "8",width = 5,command = lambda:show("8"))
mul = Button(a,text = "*",width = 5,command = lambda:show("*"))

four = Button(a,text = "4",width = 5,command = lambda:show("4"))
five = Button(a,text = "5",width = 5,command = lambda:show("5"))
six = Button(a,text = "6",width = 5,command = lambda:show("6"))
subtr = Button(a,text = "-",width = 5,command = lambda:show("-"))

one = Button(a,text = "1",width = 5,command = lambda:show("1"))
two = Button(a,text = "2",width = 5,command = lambda:show("2"))
three = Button(a,text = "3",width = 5,command = lambda:show("3"))
plus = Button(a,text = "+",width = 5,command = lambda:show("+"))

zero = Button(a,text = "0",width = 12,command = lambda:show("0"))
dot = Button(a,text = ".",width = 5,command = lambda:show("."))
equ = Button(a,text = "=",width = 5,command = cal)

cb.grid(row = 1,column = 0)
deln.grid(row = 1,column = 1)
div.grid(row = 1,column = 2)
div2.grid(row = 1,column = 3)

seven.grid(row = 2,column = 0)
eight.grid(row = 2,column = 1)
nine.grid(row = 2,column = 2)
mul.grid(row = 2,column = 3)

four.grid(row = 3,column = 0)
five.grid(row = 3,column = 1)
six.grid(row = 3,column = 2)
subtr.grid(row = 3,column = 3)

one.grid(row = 4,column = 0)
two.grid(row = 4,column = 1)
three.grid(row = 4,column = 2)
plus.grid(row = 4,column = 3)

zero.grid(row = 5,column = 0,columnspan = 2)
dot.grid(row = 5,column = 2)
equ.grid(row = 5,column = 3)

a.mainloop()




