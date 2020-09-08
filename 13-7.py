import random
print("第1000期大樂透")

a = random.randint(1,8)

b = random.sample(range(1,50),6)

print("特別號:",a)

for c in sorted(b):
    print(c, end =" ")



"""自己用的
import random
print("第1000期大樂透")

a = random.randint(1,8)

b = sorted(random.sample(range(1,50),6))

print("特別號:",a)
print(b)"""


