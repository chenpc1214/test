print("please choose 1 or 2")
choice=input("(1)F change to C\n(2)C change to F\n=" )
ch = eval(choice)

if ch==1:
    f=int(input("what is your F:"))
    resultc =f*(9/5) +32
    print("華氏%d等於攝氏%4.1f"%(f,resultc))
elif ch==2:
    c = eval(input("what is your C:"))
    resultf = (c-32)*5/9
    print("攝氏%d等於華氏%4.1f"%(c,resultf))
else:
    print("你他媽有眼睛嗎?")
