import numpy as np

a = [88,108]
b = [25,35,45,55]

agcd = np.gcd.reduce(a)
bgcd = np.gcd.reduce(b)

alcm = np.lcm.reduce(a)
blcm = np.lcm.reduce(b)

print(a,"最大公因數是",agcd)
print(b,"最大公因數是",bgcd)
print(a,"最小公倍數是",alcm)
print(b,"最小公倍數是",blcm)
