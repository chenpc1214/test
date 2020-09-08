a = input("請輸入文字:")

file_name = "ini15_6.txt"

try:
    with open (file_name,"at") as name:
        data = name.write(a)

except FileNotFoundError:
    print("查無此檔案")

else:
    b = a.split()
    c = len(b)
    print("%s  文章的字數為 %d 個字"%(file_name,c))
