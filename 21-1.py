import json
total = 0

with open ("populations.json","rt") as file:
    data = json.load(file)

    for i in data :
        if i["Year"] == "2000":
            if i['Country Name'] != "World":
                all_people = int(float(i["Numbers"]))
                total += all_people
                print(i["Country Name"]  ,"人口數=",i["Numbers"])
                
print("人口總數 = ",total)
