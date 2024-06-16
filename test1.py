import pandas

df = pandas.read_csv("GoogleApps.csv")


#df.head()
#df.info()
#df.tail()
#print(df.describe())

print(df["Rating"].max()) # максимальне значення стовпця "Rating"

print(df[df["Rating"] > 4.9]) # рядки значення стовпця "Rating" якого бiльшi ща 4.9
print(df[df["Rating"] > 4.9]["Category"]) # Значення стовпця "Category", рейтинг яких бiльшi за 4.9
print(df[df["Rating"] > 4.9]["Category"].min()) # мiнiмальне значення стовпця "Category", рейтинг яких бiльшi за 4.9

print(df[ (df["Rating"] > 4.9) & (df['Type'] == 'Free')]['Installs'].mean())

print(df[ (df["Category"] == 'ART_AND_DESIGN')]['Installs'].median())

print(df[df['Type'] != 'Free']["Price"].min())

a = df[df["Type"] == 'Free']['Reviews'].max()
b = df[df["Type"] != 'Free']['Reviews'].max()

print(a - b)

print(df[df["Content Rating"] == 'Teen']['Size'].min())

d = df["Reviews"].max()
print(df[df["Reviews"] == d]['Category'])
