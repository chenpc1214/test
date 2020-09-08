number = 0
begin = 0
answer = 30

while number != answer:
    number = int(input("請輸入1-100間的數字:"))
    
    if number > answer:
        begin+=1
        print("在小一點")
        
    elif number < answer:
        begin+=1
        print("在大一點")
        
    else:
        begin+=1
        print("恭喜答對")

print("總共猜了%d次"%begin)
