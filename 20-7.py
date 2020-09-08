import matplotlib.pyplot as mp

data1 = [1,2,3,4,5,6,7,8]
data2 = [1,4,9,16,25,36,49,64]
seq = [1,2,3,4,5,6,7,8]

mp.figure(1)
mp.plot(seq,data1,"-*")
mp.title("Test chart 1",fontsize = 20)
mp.xlabel("x-Data",fontsize = 12)
mp.ylabel("y-Data",fontsize = 12)

mp.figure(2)
mp.plot(seq,data2,"-o")
mp.title("Test chart 2",fontsize = 20)
mp.xlabel("x-value",fontsize = 12)
mp.ylabel("y-value",fontsize = 12)

mp.show()
