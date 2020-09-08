print("輸入數字判斷程式")

number = eval(input("請輸入任意整數值:"))

if number > 0:
    new_num = 0-number
    print(new_num)
else:
    print(abs(number))
    


