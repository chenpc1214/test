import Mymath

print("請輸入運算")
print("1.加法\n2.減法\n3.乘法\n4.除法")
num = int(input("輸入1/2/3/4:"))
a = int(input("a = "))
b = int(input("b = "))

if num == 1:
    print("a + b = ", MyMath.add(a, b))   # 輸出a-b字串和結果
elif num == 2:
    print("a - b = ", MyMath.sub(a, b))   # 輸出a-b字串和結果
elif num == 3:
    print("a * b = ", MyMath.mul(a, b))   # 輸出a*b字串和結果
elif num == 4:
    print("a / b = ", MyMath.div(a, b))   # 輸出a/b字串和結果
else:
    print("運算方法輸入錯誤")
