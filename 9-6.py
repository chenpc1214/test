armys = []                      

for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)

print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)

for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'

print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

for soldier in armys[47:50]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'green'
        soldier['score'] = 10
        soldier['speed'] = 'fast'

print("列印編號47到49小兵資料")
for soldier in armys[47:50]:
    print(soldier)   
