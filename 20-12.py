import matplotlib.pyplot as mp
import twstock

name1 = twstock.Stock("2890")
name2 = twstock.Stock("5880")
name3 = twstock.Stock("2886")

take1 = name1.price
take2 = name2.price
take3 = name3.price

mp.plot(take1,"-*",label = "FB")
mp.plot(take2,"-o",label = "TCB")
mp.plot(take3,"-^",label = "MB")

mp.xlabel("last 31 days")
mp.ylabel("price")
mp.legend(loc = "best")
mp.title("Three famous banks",fontsize = 20)

mp.show()
