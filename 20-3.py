import matplotlib.pyplot as mp
import numpy as np

left = np.pi* -2
right = np.pi * 2

x = np.linspace(left,right,100)
y = np.sin(2*x)

mp.plot(x,y)
mp.fill_between(x,1,y,color = "red")

mp.show()
