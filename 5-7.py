print("today is Sunday")

a = eval(input("enter date numbers:"))

if a == 1 or a%7==1:
    print("monday")
elif a == 2 or a%7==2:
    print("tuesday")
elif a == 3 or a%7==3:
    print("wensday")
elif a == 4 or a%7==4:
    print("thursday")
elif a == 5 or a%7==5:
    print("friday")
elif a ==6 or a%7==6:
    print("saturday")
else:
    print("sunday")
    
