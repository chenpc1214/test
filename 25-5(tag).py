# ex25_5.py
import pandas as pd
import numpy as np

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame([chinese, eng, math, nature, social],
                  columns = course,
                  index = range(1,6))
total = [df.iloc[i].sum() for i in range(0,5)]
df['Total'] = total

df = df.sort_values(by='Total', ascending=False)

rank = range(1,6)
df['Ranking'] = rank

for i in range(1,5):
    if df.iat[i,5] == df.iat[i-1,5]:
        df.iat[i,6] = df.iat[i-1,6]

df = df.sort_index()

ave = df.mean()
df.loc['Average'] = ave
df.iat[5,6] = np.nan

print(df)

df.to_csv('ex25_5.csv')





