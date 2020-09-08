import requests
import pandas as pd
import matplotlib.pyplot as mp

#第一步驟:下載iris資料檔，並寫入csv

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris = requests.get(url)

with open("iris.csv","wb")as openfile:
    for writeall in iris.iter_content(10240):
        data = openfile.write(writeall)

#第二步驟:讀取csv並轉換成dataframe模式

name = ["sl","sw","pl","pw","sp"]
flower = pd.read_csv("iris.csv",names = name)

#第三步驟:分類花種

first = flower[flower["sp"]=="Iris-setosa"]
second = flower[flower["sp"]=="Iris-versicolor"]
third = flower[flower["sp"]=="Iris-virginica"]

#第四步驟:繪圖

mp.plot(first['pl'],first['pw'],
         '*',color='g',label='setosa')

mp.plot(second['pl'],second['pw'],
         'x',color='b',label='versicolor')

mp.plot(third['pl'],third['pw'],
         '.',color='r',label='virginica')

mp.xlabel('Petal Length')
mp.ylabel('Petal Width')
mp.title('Iris Petal length and width anslysis')
mp.legend()
mp.show()
