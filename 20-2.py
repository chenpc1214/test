import matplotlib.pyplot as mp
import numpy as np

left = np.pi* -2
right = np.pi * 2
x = np.linspace(left,right,50)

f1 = 3*np.sin(x)
f2 = np.sin(x)
f3 = 0.2*np.sin(x)

mp.plot(x,f1)
mp.plot(x,f2,"-x")
mp.plot(x,f3,)
mp.plot(x,f1,"go")

mp.show()
