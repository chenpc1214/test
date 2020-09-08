import os
os.chdir("C:\\Users\\user\\Desktop\\Python 3.7\\python王者歸來\\解答")


def open_file(arg):
    try:
        with open (str(arg),"rt") as name:
            data = name.read()

    except FileNotFoundError:
        print("查無此檔")

    else:
        b = data.split()
        c = len(b)
        print("%s  文章的字數是 %d 個字" %(a,c))


sth_list = []

for circle in range(1,6):
    
    a = input("請輸入檔名:")
    sth_list.append(a)

for result in sth_list:
    open_file(result)
