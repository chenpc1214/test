from tkinter import *
from tkinter import messagebox

def message1():
    messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")    
def message2():
    messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
def message3():
    messagebox.showinfo("剪下內容","可在此剪下文件內容")
def message4():
    messagebox.showinfo("複製內容","可在此複製文件內容")
def message5():
    messagebox.showinfo("貼上內容","可在此貼上文件內容")
    
def about():
    messagebox.showinfo("程式說明","作者:洪錦魁")
    
a = Tk()
a.title("test")
a.geometry("300x160")


fm = Menu(a)
a.config(menu = fm)

sm = Menu(fm)

fm.add_cascade(label = "檔案", menu = sm)
sm.add_command(label = "開啟新檔",command = message1)
sm.add_separator()
sm.add_command(label = "開啟舊檔",command = message2)
sm.add_separator()
sm.add_command(label = "結束",command = a.quit)
sm.add_separator()

thirm = Menu(fm)

fm.add_cascade(label = "編輯", menu = thirm)
thirm.add_command(label = "剪下",command = message3)
thirm.add_separator()
thirm.add_command(label = "複製",command = message4)
thirm.add_separator()
thirm.add_command(label = "貼上",command = message5)
thirm.add_separator()

fourthm = Menu(fm)

fm.add_cascade(label = "說明", menu = fourthm)
fourthm.add_command(label = "程式說明",command = about)
fourthm.add_separator()

mainloop()
