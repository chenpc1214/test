from tkinter import *

def myfun():
    monthrate = interest.get() / (12*100)
    loan = loanmoney.get()
    molecules = loan * monthrate
    denominator = 1-(1/(1+monthrate) ** (years.get() * 12))
    monthpaid = int(molecules / denominator)
    monthpayment.set(monthpaid)
    totalpaid = int(monthpaid * 12 * years.get())
    totalpayment.set(totalpaid)
        
window = Tk()
window.title("ex18_4")                  # 視窗標題

Interest = Label(window, text="利率")
Years = Label(window, text="貸款年數")
LoanMoney = Label(window, text="貸款金額")
MonthPayment = Label(window, text="每月支付金額")
TotalPayment = Label(window, text="總支付金額")

interest = DoubleVar()
years = IntVar()
loanmoney = IntVar()
monthpayment = IntVar()
totalpayment = IntVar()

interestE = Entry(window, textvariable=interest)
yearsE = Entry(window, textvariable=years)
loanmoneyE = Entry(window, textvariable=loanmoney)
monthpaymentL = Label(window, textvariable=monthpayment, bg='lightyellow')
totalpaymentL = Label(window, textvariable=totalpayment, bg='lightyellow')

Interest.grid(row=0, column=0)
Years.grid(row=1, column=0)
LoanMoney.grid(row=2, column=0)
MonthPayment.grid(row=3, column=0)
TotalPayment.grid(row=4, column=0)

interestE.grid(row=0, column=1, padx=2)
yearsE.grid(row=1, column=1, padx=2)
loanmoneyE.grid(row=2, column=1, padx=2)
monthpaymentL.grid(row=3, column=1, padx=2)
totalpaymentL.grid(row=4, column=1, padx=2)

btnExec = Button(window, text="計算", command=myfun)
btnExec.grid(row=5, column=1, pady=2)




"""自己做的

from tkinter import *

def cal():
    mr= e3.get()/(12*100)
    loan = e3.get()
    molecules = loan*mr
    denominator = 1-(1/(1+mr) ** (e2.get() * 12))
    monthpaid = int(molecules / denominator)
    e4.set(monthpaid)
    totalpaid = int(monthpaid * 12 * e2.get())
    e5.set(totalpaid)

a = Tk()
a.title("利率計算器")

e1 = DoubleVar()
e2 = IntVar()
e3 = IntVar()
e4 = IntVar()
e5 = IntVar()


lab1 = Label(a,text = "利率",width = 5).grid(row = 0,column = 0)
lab2 = Label(a,text = "貸款年數",width = 5).grid(row = 1,column = 0)
lab3 = Label(a,text = "貸款金額",width = 5).grid(row = 2,column = 0)
lab4 = Label(a,text = "月付金",width = 5).grid(row = 3,column = 0)
lab5 = Label(a,text = "總支出",width = 5).grid(row = 4,column = 0)

E1 = Entry(a, width = 15,textvariable = e1).grid(row = 0,column = 1)
E2 = Entry(a, width = 15,textvariable = e2).grid(row = 1,column = 1)
E3 = Entry(a, width = 15,textvariable = e3).grid(row = 2,column = 1)
L4 = Label(a, width = 2,textvariable = e4).grid(row = 3,column = 1)
L5 = Label(a, width = 2,textvariable = e5).grid(row = 4,column = 1)

but = Button(a, text = "計算",command = cal).grid(row =5,column = 1)

a.mainloop()"""
