import matplotlib.pyplot as mp
import twstock

name = twstock.Stock("2330")

take = name.price
high = name.high
low = name.low


mp.plot(take,"-*",label = "Closing price")
mp.plot(high,"-o",label = "high")
mp.plot(low,"-^",label = "low")
mp.xlabel("last 31 days")
mp.ylabel("price")
mp.legend(loc = 2)
mp.title("TSMC",fontsize = 20)

mp.show()
