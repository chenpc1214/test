a = "chickens"
for aaa in range (99, 0, -1,):
    print(aaa, a, "of brood on the groung.")
    print(aaa, a, "of beer.")
    print("take one leave.")
    print("pass it to the framer.")
    if aaa == 1:
        print("no chicken can bring.")
    else:
        aaaa = aaa - 1
        if aaaa == 1:
           a = "chicken"
        print(aaaa, a, "of brood on the ground.")
    print()
