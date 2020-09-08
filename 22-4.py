import csv
import matplotlib.pyplot as mp

a,b,c = [],[],[]

with open("TaipeiWeatherJan.csv","rt") as file:
    data = csv.reader(file)
    next_data = next(data)
    listcsv = list(next_data)
    for row in data:
        a.append(int(row[1]))
        b.append(int(row[2]))
        c.append(int(row[3]))

seq = range(1,32)        
mp.plot(seq,a)
mp.plot(seq,b)
mp.plot(seq,c)
mp.title("Weather Report Jan.2017",fontsize = 30)
mp.xlabel("", fontsize=14)
mp.ylabel("temperature(c)",fontsize = 18)
mp.tick_params(axis = "both",labelsize = 15,color = "red")
mp.show()
