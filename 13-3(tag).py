import random


b = random.randint(1,30)
count = 0
while True :
    a = input("請輸入1~30間的數字:")
    if a == "Q" or a== "q":
        break
    
    newa =int(a)
    count += 1
    
    if newa == b:
        print("恭喜答對")
        print("總共猜對了%d次"%count)
        break

    elif newa < b :
        print("請猜大一點")

    else:
        print("請猜小一點")


"""
自己做的
import random

a = input("請輸入1~30間的數字:")
b = random.randint(1,30)

while True :
    if a == "Q" or "q":
        break

    elif a ==b:

        c = count(a)
        
        print("恭喜答對")
        print("總共猜對了%d次"%c)

    elif a > b :
        print("請猜小一點")

    else:
        print("請猜大一點")"""
