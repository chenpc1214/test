the_hightest = (30,28,29,31,33,35,32)
the_lowest =   (20,21,19,22,23,24,20)
a = max(the_hightest)
b = min(the_lowest)

print("過去一周最高溫度:",a)
print("過去一周最低溫度:",b)
print("過去一周平均溫度")
for i in range(len(the_hightest)):
    print("%3.1f  " % ((the_hightest[i]+the_lowest[i])/2), end="")
    
    
