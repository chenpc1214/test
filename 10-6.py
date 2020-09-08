c = {c for c in range(1,100,2)}
d = {d for d in range(0,101,5)}

print("聯集:",c|d)
print("交集:",c&d)
print("A-B差集:",c-d)
print("B-A差集:",d-c)
