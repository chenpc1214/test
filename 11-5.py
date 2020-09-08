def add(n1, n2):
    return n1 + n2
    
def sub(n1,n2):
    return n1 -n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

while True:
    
    a =int(input("請輸入第一個數字:"))
    b =int(input("請輸入第二個數字:"))
    c = input("請輸入運算子((+ - * / ):")

    if c ==  "+":
        print ("計算結果=", add(a,b))

    elif c == "-":
        print ("計算結果=",sub(a,b))
            
    elif c == "*":
        print ("計算結果=",mul(a,b))
            
    elif c == "/":
        print ("計算結果=",div(a,b))
            
    else:
        print("請輸入正確的公式")
    d = input("是否繼續?(Y or y=繼續) : ")
    if d == "Y" or d == "y":
        pass
    else:
        break
    


