mark =""

with open ("ex14_6_1.txt") as name:
    data = name.readlines()
    
for result in data:
     mark +=result.rstrip()

print(mark)
