from tkinter import *

a = Tk()
a.title("enterprise")

lab =  Label(a, width=15 ,text = "a 企業",bg = "red")
lab2 = Label(a, width=15 ,text = "b 企業",bg = "orange")
lab3 = Label(a, width=15 ,text = "c 企業",bg = "yellow")
lab4 = Label(a, width=15 ,text = "d 企業",bg = "green")
lab5 = Label(a, width=15 ,text = "e 企業",bg = "gold")

lab.pack(side = TOP)
lab2.pack(side = TOP)
lab3.pack(side = TOP)
lab4.pack(side = TOP)
lab5.pack(side = TOP)

a.mainloop()

