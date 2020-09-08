f = [32,77,104]
new_f = []
for c in f:
    c = (c-32)*5/9
    new_f.append(round(c,1))
print(new_f)
