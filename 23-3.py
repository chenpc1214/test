import numpy as np

a = np.ones((3,2),dtype="int8")
a += 1

b = np.array([[1,4],[2,5],[3,6]])

print("A = ")
print(a)

print("B = ")
print(b)

print("A + B = ")
print(a+b)

print("A - B = ")
print(a-b)

print("A * B = ")
print(a*b)

print("A / B = ")
print(a/b)

print("A % B = ")
print(a%b)

print("A 轉置 = ")
print(a.reshape(2,3))

print("B 轉置 = ")
print(b.reshape(2,3))


