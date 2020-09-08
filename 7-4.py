begin = eval(input("今年體重:"))
killogram = eval(input("如果每年固定增加(kg):"))
year = eval(input("請輸入年:"))

for numbers in range(1,year+1):
    result = begin + (killogram*numbers)
    round_result = round(result,1)
    print("第 %d 年的體重"%(numbers),result)
    
