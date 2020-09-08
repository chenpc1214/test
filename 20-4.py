import matplotlib.pyplot as mp
import random

def fetchn(arg):
    
    xr = random.choice([1,2,3,-1,-2,-3])
    yr = random.choice([1,3,5,-1,-3,-5])

    xm = x[arg-1] + xr
    ym = y[arg -1] + yr

    x.append(xm)
    y.append(ym)

num = 10000
x = [0]
y = [0]

while True:

    for i in range(1,num):
        fetchn(i)
    t = x
    mp.scatter(x,y,cmap = "summer")
    mp.show()
    ask = input("繼續嗎??")

    if ask =="n" or ask =="N":
        break

    else:
        x[0] = x[num-1]
        y[0] = y[num-1]
        del x[1:]
        del y[1:]
