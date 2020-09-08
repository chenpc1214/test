list1=[i for i in range(1,10)]
f=""
for o in list1:
    f=str(o)+f
    print("{0:>9}".format(f))
    
"""原先方法
n = 1
for x in range(1,10):
    for y in range(1,n+1):
        if x>y:
            n+=1
            print(y,end="")
    print()
                            """
