
from tkinter import *
from tkinter import messagebox

def printInfo():                    
    if e1.get() in ad:
        if e2.get() == ad[e1.get()]:
            messagebox.showinfo(title = "歡迎進入系統",message = "登入成功")
        else:
            messagebox.showinfo(title = "拒絕進入系統",message = "密碼錯誤")
    else:
        messagebox.showinfo(title = "拒絕進入系統",message = "帳號錯誤")

ad = {"AAA":"1234","BBB":"5678","CCC":"9999"}

a = Tk()
a.title("登入系統")

lab1 = Label(a, text = "Account").grid(row = 0,column = 0)
lab2 = Label(a, text = "Password").grid(row = 1,column = 0)

acc = StringVar()
pas = StringVar()

e1 = Entry(a, textvariable = acc)
e2 = Entry(a, textvariable = pas)
e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)

but = Button(a,text = "確認",command = printInfo)
but.grid(row = 2,column = 1,pady = 10)

a.mainloop()
