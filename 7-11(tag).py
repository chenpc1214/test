n = 10
for i in range(1,n):
    for j in range(n-i,0,-1):
        print(" ", end='')
        
    for k in range(i,0,-1):
        print(k, end='')
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

