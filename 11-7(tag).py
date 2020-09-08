def CtoF(c):
   f = 9 / 5 *c+32
   return f

def FtoC(f):
    c = (5/9)*(f - 32)
    return c

tem = 21
tem2 = 70

print("攝氏溫度","      ","華氏溫度","      ","|","      ""華氏溫度","      ","攝氏溫度")
print("="*64)

for a in range(1,10):
    print("  %3d            %6.2f         |         %3d            %6.2f "%(tem,CtoF(tem),tem2,FtoC(tem2)))
    tem +=1
    tem2 +=5
