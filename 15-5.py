
def div(arg1,arg2):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        return arg1/arg2

    except Exception:
        print("資料型態錯誤")





while True:
    a = input("請輸入第一個數字:")
    b = input("請輸入第二個數字:")
    print(div(a,b),"\n")
    c = input("是否續(y|n)? 輸入n或N代表不繼續:")
    print("\n")
    if  c == "n" or c=="N":
        break
    



