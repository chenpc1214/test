import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)           
    dates, highTemps, meanTemps, lowTemps = [], [], [], [] 
    for row in csvReader:
        try:                    
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])          
            meanTemp = int(row[2])          
            lowTemp = int(row[3])           
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)      
            meanTemps.append(meanTemp)      
            lowTemps.append(lowTemp)        
            dates.append(currentDate)       

fig = plt.figure(dpi=80, figsize=(12, 8))   
plt.plot(dates, highTemps, label='High')    
plt.plot(dates, meanTemps, label='Mean')    
plt.plot(dates, lowTemps, label='Low')      
plt.fill_between(dates, highTemps, meanTemps, color='y', alpha=0.2) 
plt.fill_between(dates, meanTemps, lowTemps, color='r', alpha=0.2)  
fig.autofmt_xdate()                         
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.legend(loc='best')
plt.show()
