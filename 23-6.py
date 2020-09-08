import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(0,2,20)
xn = x*np.pi
y = np.cos(xn)
xvalue = np.linspace(0,2,100)
yinterp = np.interp(xvalue,x,y)

mp.plot(x,y,"o")
mp.plot(xvalue,yinterp,"-x")
mp.show()
