title_row = "9 * 9 Multiplication Table"
a = title_row.center(40)
print(a)
number_row =1,2,3,4,5,6,7,8,9
print("%4d%4d%4d%4d%4d%4d%4d%4d%4d"%number_row)


print("="*42)

for y in range(1,10):
    print(y,"|",end="")
    for z in range(1,10):
        result = y*z
        print("%3d"%(result),end=" ")
    print()



    


    
