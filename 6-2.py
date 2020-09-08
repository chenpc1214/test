from copy import deepcopy

old = "Toyota","Nissan","Honda"
list_old = list(old)

list_new = deepcopy(list_old)
list_new.pop(1)
list_new.insert(1,"Ford")

print("舊的銷售品牌:",list_old)
print("新的銷售品牌:",list_new)

