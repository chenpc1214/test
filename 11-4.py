a =int(input("請輸入第一個數字:"))
b =int(input("請輸入第二個數字:"))
c = input("請輸入運算子((+ - * / ):")

def add(n1, n2):
    return n1 + n2
    
def sub(n1,n2):
    return n1 -n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

if c is  "+":
    print ("計算結果=",add(a,b))

elif c is "-":
    print ("計算結果=",sub(a,b))
    
elif c is "*":
    print ("計算結果=",mul(a,b))
    
elif c is "/":
    print ("計算結果=",div(a,b))
    
else:
    print("公式輸入錯誤")
