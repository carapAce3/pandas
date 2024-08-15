import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('GoogleApps.csv')

#print(df[df['gender'] == 'male']['math score'])

#df[df['race/ethnicity'] == 'group C']['reading score'].plot(kind='hist')

#df['math score'].plot(kind='hist')

#df['math score'].plot(kind='box')

#df.plot(x = 'race/ethnicity', y = 'math score', kind='scatter')

#df['race/ethnicity'].value_counts().plot(kind='pie')

df[df['Category'] == 'ART_AND_DESIGN']['Rating'].value_counts().plot(kind='bar')




plt.show()