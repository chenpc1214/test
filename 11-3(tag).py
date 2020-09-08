def reverse(n):
   while n != 0:
        r = n % 10
        print(r, end='')
        n//= 10
        

x = eval(input("請輸入1個數值 = "))
reverse(x)
