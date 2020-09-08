import pandas as pd
import matplotlib.pyplot as mp

All = {"pop":[1000, 850, 800, 1500, 600, 800],
       "area":[400,500,850,300,200,320],
       "town":["NY","Chic","Bankg","Tk","Sig","Hk"]}

ap = pd.DataFrame(All,columns = ["pop","area","town"],index =All["town"] )

density = ap['pop'].div(All['area'])

ap["density"] = density
print(ap)

ap.plot(title = "city st")
mp.xlabel("city")

all_figure_thing,first_ax = mp.subplots()
all_figure_thing.suptitle("city st")

first_ax.set_xlabel("city")
first_ax.set_ylabel("population")

second_ax = first_ax.twinx()
second_ax.set_ylabel("density")

ap['pop'].plot(ax=first_ax,rot=90)     
ap['area'].plot(ax=first_ax, style='g-')     
ap['density'].plot(ax=second_ax, style='r-')


first_ax.legend(loc=1)
second_ax.legend(loc = 2)
mp.show()
