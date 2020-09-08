import numpy as np
import matplotlib.pyplot as mp

mean,sigmas = 100,15

a = np.random.normal(mean,sigmas,10000)
mp.hist(a,bins = 50)
mp.show()
