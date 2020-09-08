import csv

t2015=0
t2016=0


with open("csvReport.csv","rt") as file:
    data = csv.reader(file)
    listcsv =list(data)

for row in listcsv :
    if row[1] =="2016":
        t2015 += int(row[5])
else:
    t2016 += int(row[5])
    
print("Total Revenue of 2015 = ",t2015)
print("Total Revenue of 2015 = ",t2016)
