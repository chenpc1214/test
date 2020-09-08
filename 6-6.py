
s1="student1",80,95,88,0,0
s2="student2",98,97,96,0,0
s3="student3",90,91,92,0,0
s4="student4",91,93,95,0,0
s5="student5",92,97,90,0,0

a= list(s1)
b= list(s2)
c= list(s3)
d= list(s4)
e= list(s5)
table = [a,b,c,d,e]

def total(number):
    return sum(table[number][1:4])

def average(number):
    return round(total(number)/3,1)

t1=table[0][4] = total(0)
t2=table[1][4] = total(1)
t3=table[2][4] = total(2)
t4=table[3][4] = total(3)
t5=table[4][4] = total(4)

a1=table[0][5] = average(0)
a2=table[1][5] = average(1)
a3=table[2][5] = average(2)
a4=table[3][5] = average(3)
a5=table[4][5] = average(4)

print(table[0])
print(table[1])
print(table[2])
print(table[3])
print(table[4])

#這也可以寫成print(table[0],table[1],table[2],table[3],table[4],sep = "\n")
