from tkinter import *

window = Tk()
window.title("ex18_2")              
lab1 = Label(window,text="Peter",
              bg="lightyellow",     
              width=15)             
lab2 = Label(window,text="John",
              bg="lightgreen",      
              width=15)             
lab3 = Label(window,text="Notron",
              bg="lightblue",       
              width=15)             
lab4 = Label(window,text="Kevin",
              bg="lightgreen",      
              width=15)         
lab5 = Label(window,text="Tommy",
              bg="lightblue",   
              width=15)             
lab6 = Label(window,text="Mary",
              bg="lightyellow",     
              width=15)             
lab7 = Label(window,text="Tracy",
              bg="lightblue",
             width=15)             
lab8 = Label(window,text="Mike",
              bg="lightyellow",     
              width=15)             
lab9 = Label(window,text="Vicent",
              bg="lightgreen",      
              width=15)             

lab1.grid(row=0,column=0)           
lab2.grid(row=0,column=1)           
lab3.grid(row=0,column=2)           
lab4.grid(row=1,column=0)           
lab5.grid(row=1,column=1)           
lab6.grid(row=1,column=2)           
lab7.grid(row=2,column=0)
lab8.grid(row=2,column=1)
lab9.grid(row=2,column=2)


"""from tkinter import *  自己做的

a = Tk()
a.title("people name")

nl = ["peter","john","notron","kevin","tommy","mary","tracy","mike","vicent"]

nn = len(nl)

for i in range(1,nn+1):
    lab = Label(a,width = 6,  text =nl[0:9] )

for x in range(0,3):
    for y in range(0,3):
        lab.grid(row = x, column = y)

a.mainloop()"""
