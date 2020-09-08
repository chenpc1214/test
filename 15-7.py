import os , traceback

os.chdir("C:\\Users\\user\\Desktop\\Python 3.7\\python王者歸來\\解答")

def open_file(arg):
    try:
        with open (arg,"rt") as name:
            data = name.read()

    except FileNotFoundError :
        print("查無此檔")

    else:
        b = data.split()
        c = len(b)
        print("%s  文字字數是 %d 個字"%(arg,c))
        return c

def countword(arg):
    wdlen = open_file(arg)
    
    if wdlen < 10:
        raise Exception ("檔案長度太長")
    if wdlen > 35:
        raise Exception("檔案長度過短")
    print("檔案長度正確")

for final in ("d1.txt","d2.txt","d3.txt","d4.txt","d5.txt"):
    try:
        countword(final)
    except Exception as err:
        with open ("errdata(改).txt","at") as name:
            name.write(traceback.format_exc())
            print("將Traceback寫入錯誤檔案 errdata(改).txt  完成")
            print("檔案長度檢查異常發生: ", str(err))
    

    
