import pandas as pd

df = pd.read_csv('data.csv')
df2 = pd.read_json('data.json')
# print(df)
# print(df.head())

print(df.to_string())
print(df2.to_string())