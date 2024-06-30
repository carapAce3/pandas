import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')
print(len(df[pd.isnull(df["Rating"])]))
df['Rating'].fillna(1, inplace=True)
print(len(df[pd.isnull(df["Rating"])])) # 0

print(df["Size"].value_counts()) 

print(df[df["Category"] == 'Tools']['Size'])

df['Profit'] = df['Rating'] * df['Price']