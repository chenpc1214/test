tp = (1,2,3,4,5,2,3,1,4)
newtp = list(tp)
newlst = []

for x in newtp:
    if x not in newlst:
        newlst.append(x)
newtp = tuple(newlst)
print("新的元組內容 : ", newtp)
        
    
        
