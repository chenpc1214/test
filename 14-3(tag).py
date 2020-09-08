import os

amountsize = 0
amountfile = 0

a = input("請輸入目錄:")

if os.path.exists(a):
    for name in os.listdir(a):
        data = os.path.getsize(os.path.join(a,name))
        print(name, ":", data)
        amountsize += data
        amountfile += 1
    print("全部檔案數量是 = ", amountfile)    
    print("全部檔案大小是 = ", amountsize)
else:
    print(a,"目錄不存在")
