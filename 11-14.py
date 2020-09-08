def even(number):
    return number if number % 2 ==0 else None

number = [5,10,15,20,25,30]
nf = filter(even,number)
print("偶數串列:",[result for result in nf] )
