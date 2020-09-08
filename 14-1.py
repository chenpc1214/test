import os

a = input("請輸入此目錄:")

if os.path.exists(a):
    print(a,"已經存在")
else:
    print("此目錄不存在")
    print("建立此目錄")

    
