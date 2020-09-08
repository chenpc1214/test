A = []
for i in range(1,100,2):
    A.append(i)
B = []
for i in range(0,101,5):
    B.append(i)
aSet = set(A)                   
bSet = set(B)                   

unionAB = aSet | bSet
print("聯集 : ", unionAB)
interAB = aSet & bSet
print("交集 : ", interAB)
A_B = aSet - bSet
print("A-B差集 : ", A_B)
B_A = bSet - aSet
print("B-A差集 : ", B_A)
