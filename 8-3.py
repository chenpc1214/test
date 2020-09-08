name =("John","Peter","Curry","Mike","Kevin")

print("原先讀書會成員")

for oname in name:
    print(oname)

list_name = list(name)
list_name.append("Marry")
list_name.append("Tom")
list_name.insert(7,"Carlo")

tuple_name = tuple(list_name)

print("新的讀書會成員")

for newname in tuple_name:
    print(newname)
