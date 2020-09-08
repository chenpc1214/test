def pi(arg):
    result = 0
    for r_result in range(1,arg+1,1):
        result += 4*((-1)**(r_result+1)/(2*r_result-1))
    return result

print("   i    PI")
print("="*16)

for a in range(1,10000,1000):
    b = pi(a)
    print("%5d   %7.5f"%(a,b))
