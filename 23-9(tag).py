import numpy as np
import matplotlib.pyplot as plt

w = np.loadtxt("weatherTaipei.txt",delimiter=',',skiprows=1,usecols=(1,2,3))
x = np.arange(1, 32)

high = w[:,0]
lineHigh, = plt.plot(x, high, '-o', label="High")

ave = w[:,1]
lineAve, = plt.plot(x, ave, '-^', label="Average")

low = w[:,2]
lineLow, = plt.plot(x, low, '-x', label="Low")

plt.legend(handles=[lineHigh, lineAve, lineLow], loc='best')
plt.title("Taipei Weather Report", fontsize=24)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Temperature", fontsize=14)

plt.show()
