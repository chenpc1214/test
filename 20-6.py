import matplotlib.pyplot as mp

data1 = [1,2,3,4,5,6,7,8]
data2 = [1,4,9,16,25,36,49,64]
data3 = [1,3,6,10,15,21,28,36]
data4 = [1,7,15,26,40,57,77,100]
data5 = [1,6,11,16,21,26,31,36]
seq = [1,2,3,4,5,6,7,8]

mp.subplot(2,3,1)
mp.plot(seq,data1,"-*")
mp.subplot(2,3,2)
mp.plot(seq,data2,"-o")
mp.subplot(2,3,3)
mp.plot(seq,data3,"-^")
mp.subplot(2,3,4)
mp.plot(seq,data4,"-s")

mp.subplot(2,3,6)
mp.plot(seq,data5,"-v")

mp.show()
