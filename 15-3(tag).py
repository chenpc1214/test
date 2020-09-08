a = input("請輸入第一個數字:")
b = input("請輸入第二個數字:")

def div(arg1,arg2):
    try:
        arg1 = int(arg1)
        arg2 = int(arg2)
        return arg1/arg2

    except ValueError:
        print("除法資料型態不符合")

    except ZeroDivisionError:
        print("除數不可為0")

print(div(a,b))

