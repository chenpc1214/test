import csv

a = 0
b = 0

with open("csvReport.csv","rt") as file:
    data = csv.reader(file)
    listcsv = list(data)

for row in listcsv :
    if row[0] =="Steve":
        if row[1] =="2015":
            a += int(row[5])
        if row[1] == '2016':
            b += int(row[5])

print("Steve Total Revenue of 2015 = ",a)
print("Steve Total Revenue of 2016 = ",b)
