import numpy as np
import matplotlib.pyplot as mp

a = np.random.randint(1,6+1,10000)
b = np.random.randint(1,6+1,10000)
c = np.random.randint(1,6+1,10000)
total = a+b+c

mp.hist(total,bins = 16)
mp.show()
