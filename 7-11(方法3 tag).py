for i in range(9):
    string_line=''.join([str(num) for num in range(1,i+2)])
    print(f'{string_line:>9}')

"""原先方法
n = 1
for x in range(1,10):
    for y in range(1,n+1):
        if x>y:
            n+=1
            print(y,end="")
    print()
                            """
