import numpy as np

a = np.array([[6,5],[9,2]])
b = np.array([100,50])

line = np.linalg.solve(a,b)
print("x = ",line[0])
print("y = ",line[1])

