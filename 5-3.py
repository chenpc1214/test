x,y =eval(input("輸入點座標:"))

distance = ((0-x)**2+(0-y)**2)**0.5

if distance <= 20:
    print("點座標(%d,%d)在圓內"%(x,y))
else:
    print("點座標(%d,%d)並沒有在圓內"%(x,y))



