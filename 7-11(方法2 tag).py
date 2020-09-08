n=1
for x in range(1,10):
    print((9-x)*" ",end="") #增加這一行
    for y in range(1,n+1):
        if x>=y:
            n+=1
            print(y,end="")
    print()

"""原先方法
n = 1
for x in range(1,10):
    for y in range(1,n+1):
        if x>y:
            n+=1
            print(y,end="")
    print()
                            """
