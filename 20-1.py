import matplotlib.pyplot as mp

Benz = [3367,4120,3367,4120,5523]
BMW = [4900,4950,3590,4000,4423]
Lexus = [6200,6930,4930,5200,5230]
years = [2018,2019,2020,2021,2022]

mp.plot(years,Benz,"-^",label = "Benz")
mp.plot(years,BMW,"-x",label = "BMW")
mp.plot(years,Lexus,"-o",label = "Lexus")

mp.title("sales product",fontsize = 20)
mp.xlabel("years")
mp.ylabel("sale amount")
mp.xticks(years)
mp.tick_params(axis = "both",color = "red")
mp.legend(loc = 2)
mp.show()
