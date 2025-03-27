#Merge all the data together

import pandas as pd

#Load the data
df1 = pd.read_csv('2014_merged.csv')
df2 = pd.read_csv('2015_merged.csv')
df3 = pd.read_csv('2016_merged.csv')
df4 = pd.read_csv('2017_merged.csv')
df5 = pd.read_csv('2018_merged.csv')
df6 = pd.read_csv('2019_merged.csv')
df7 = pd.read_csv('2020_merged.csv')
df8 = pd.read_csv('2021_merged.csv')
df9 = pd.read_csv('2022_merged.csv')
df10 = pd.read_csv('2023_merged.csv')
df11 = pd.read_csv('2024_merged.csv')

#Merge all the data together
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], ignore_index=True)

#Export the data
df.to_csv('finalData.csv', index=False)