rom tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + " "
    x.set(selection)

window = Tk()
window.title("ex18_6")                     # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球",
          4:"桌球", 5:"排球"}               # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)

x = StringVar()
display = Label(window,textvariable=x, bg="lightgreen",width=30)
display.grid(row=i+3)

window.mainloop()


"""自己做的

from tkinter import *

def pr():
    lab2.set(cv.get())

cv = StringVar()
cd = {0:"美式足球",1:"棒球",2:"籃球",3:"網球",4:"撞球",5:"排球"}

a =Tk()
a.title("checkbox")

lab = Label(a,text = "選擇最喜歡的運動").grid(row = 0,column = 0)
lab2 = Label (a,text = cd.get()).grid(row = 9,column = 0)

for key,val in cd.items():
    c = Checkbutton(a,text = val,textvariable = cv)

for x in range(1,len(cd)+1):
    c.grid(row = x,column = 0)

but = Button(a,text = "確定",command = pr).grid(row = 8,column = 0)

"""
