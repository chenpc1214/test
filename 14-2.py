import os

a = input("請輸入檔案:")

if os.path.isfile(a):
    print(a,":",os.path.getsize(a),"個位元")
else:
    print(a,"檔案不存在")
    
