inside = int(input("請輸入存款本金:"))
muti = eval(input("請輸入存款年利率(percent%):"))
years = int(input("請輸入多少年:"))

for numbers in range(1,years+1):
    inside = inside * (1+muti)
    print("第%d年的本金和:%d"%(numbers,inside))
    
