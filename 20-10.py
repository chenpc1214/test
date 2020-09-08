import matplotlib.pyplot as mp

x = [10543,2105,1190,3346,980]
y = ["USA","Austrail","Japan","Eroupe","UK"]

mp.pie(x,labels = y,explode = (0,0,0.2,0,0),autopct = "%2.2f%%")

mp.show()
