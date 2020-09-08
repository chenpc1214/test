import pandas as pd

pdd = {'place':['North America', 'South America', 'Europe',
                   'Afirca', 'Asia'],
          'population':[3.8, 6.2, 7.4, 12.28, 45.45]}
result = pd.DataFrame(pdd, columns=["population"],
                      index=pdd["place"])
print(result)
