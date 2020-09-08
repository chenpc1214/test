import csv

a,b,c = [],[],[]

with open("TaipeiWeatherJan.csv","rt") as file:
    data = csv.reader(file)
    next_data = next(data)
    listcsv = list(data)
    
    for row in listcsv:
        a.append(row[1])
        b.append(row[2])
        c.append(row[3])
    
print("最高溫:",a)
print("平均溫:",b)
print("最低溫:",c)
