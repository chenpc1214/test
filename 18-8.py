from tkinter import *

a = Tk()
a.title("圖片作業")

pict = PhotoImage(file ="hung.png")

name = """的名字是陳柏政，
首先非常感謝您願意撥出寶貴的時間讓我有機會自我介紹，
我於民國86年出生在桃園市，
今年就讀於國立台中科技大學應用中文系二年級
，今年20歲"""

lab = Label(a,text = name,bg = "yellow",justify = "left",padx = 10).pack(side = "left")
lab2 = Label(a,image = pict).pack(side = "right")

