#平均值
value = (1100,652,946,821,955,1024,1155)
average = sum(value)/len(value)
print("平均值:",average)
#變異數
var=0
for v in value:
    var = var + ((v - average)**2)
    var = var/(len(value)-1)
print("變異數:",var)
#標準差
dev = 0
for v in value:
    dev = dev+((v-average)**2)
dev = (dev/(len(value)-1))**0.5
print("標準差:",dev)
