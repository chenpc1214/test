s1=1,"student1",80,95,88,0,0,0
s2=2,"student2",98,97,96,0,0,0
s3=3,"student3",90,91,92,0,0,0
s4=4,"student4",91,93,95,0,0,0
s5=5,"student5",92,97,90,0,0,0

a= list(s1)
b= list(s2)
c= list(s3)
d= list(s4)
e= list(s5)

print("原始成績",a,b,c,d,e,sep="\n")

sc = [a,b,c,d,e]

for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round((sc[i][5]/3),1)

sc.sort(key=lambda x:x[5],reverse =True)

"""print("依總分",sc[0],sc[1],sc[2],sc[3],sc[4],sep="\n")"""

"""print("填入排名(先依總分由大到小排，再加入次序)")"""
for i in range(len(sc)):
    sc[i][7] = i+1
    
    
sc.sort(key = lambda x:x[0])



for i in range(len(sc)):
    for j in range(len(sc)):
        if sc[i][6]==sc[j][6]:
            sc[i][7] = sc[j][7]
print("最後的成績單",sc[0],sc[1],sc[2],sc[3],sc[4],sep="\n")
            






