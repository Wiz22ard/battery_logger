import pandas as pd

df = pd.read_csv('charging3.csv')

print(df.loc[df['percentage'] ~= 100])
