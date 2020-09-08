import random

a = ["蘋果","香蕉","西瓜","水蜜桃","百香果"]
print("執行前串列",a)


for x in range(len(a)) :
    b = random.choice(a)
    print("刪除 : ", b)
    a.remove(b)
    print("目前串列 : ", a)
