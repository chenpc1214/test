def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("下列是前10個Fibonacci數列")
for index in range(10):
    print("%4d" % fib(index), end='')



"""
自己做的
def fib(n):
    if n<=2:
        F0 = 0
        F1 = 1
    for n in range(0,n):
        Fn = Fn -1 + Fn-2
        print(Fn)

print("下列是前十個Fibonacci數列")
print(fib(10))"""
