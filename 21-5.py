import pygal.maps.world
import json
from pygal.maps.world import COUNTRIES

#擷取國家

def getcountry(arg):
    for keycode,valname in COUNTRIES.items():
        if valname == arg:
            return keycode
    return None

#開json

with open("populations.json","rt") as file:
    data = json.load(file)

#劫data內的資料

dictdata = {}
for getdata in data :
    if getdata["Year"] =="2000":
        countryname = getdata["Country Name"]
        countrycode = getcountry(countryname)
        peo = int(float(getdata["Numbers"]))
        if countrycode != None:
            dictdata[countrycode] = peo

#開始設計

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}

for code,population in dictdata.items():
    if population > 1000000000:
        dict1[code] = population
        
    elif 50000000 <= population <= 1000000000:
        dict2[code] = population

    elif 10000000 <= population <= 50000000:
        dict3[code] = population
        
    elif 5000000 <= population <= 10000000:
        dict4[code] = population

    else:
        dict5[code] = population

mp = pygal.maps.world.World()
mp.title = "world people"
mp.add("大於一億",dict1)
mp.add("五千萬至一億之間",dict2)
mp.add("一千萬至五千萬之間",dict3)
mp.add("五百萬至一千萬之間",dict4)
mp.add("不足五百萬",dict5)

mp.render_to_file("world_people.svg")
