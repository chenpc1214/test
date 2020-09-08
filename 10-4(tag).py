a = []

for appen in range(1,100,2):
    a.append(appen)

b = []
number =2
number_two =0

while number < 100:
    if number ==2:
        b.append(number)
        number_two +=1
    else:
        for n in range(2,number):
            if number % n == 0:
                break
        else:
            number_two += 1
            b.append(number)
    number += 1

newa = set(a)
newb = set(b)

v = newa | newb
w = newa & newb
x = newa - newb
y = newb | newa
z = newa ^ newb

print("聯集:",v)
print("聯集:",w)
print("聯集:",x)
print("聯集:",y)
print("聯集:",z)


