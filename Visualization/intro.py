from __future__ import print_function
import matplotlib.pyplot as plt
import pandas as pd

df_can = pd.read_excel('Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print('Data read into a pandas dataframe!')
print(df_can.head())
print("-"*20)
print(df_can.tail())
print("-"*20)
print(df_can.info())
print("-"*20)
print(df_can.columns.values)
print(df_can.index.values)

print("-"*20)
print(df_can.shape)

print("-"*20)
#Drop Some Columns
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(3))

#Rename Columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

#Add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013
df_can['Total'] = df_can.sum(axis=1)

print(df_can.isnull().sum())

#A quick summary of each column in our dataframe using the describe() method
print(df_can.describe())

#Print the countries
print(df_can.Country)

#Filtering on the list of countries and the data for years: 1980 - 1985.
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

#Set the index to be the Country
df_can.set_index('Country', inplace=True)
print(df_can.head(3))

#Japan for year 2013
print(df_can.loc['Japan', 2013])

#Japan for years 1980 .. 1984
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])

#Convert the column names into strings: '1980' to '2013'
df_can.columns = list(map(str, df_can.columns))

#For plotting
years = list(map(str, range(1980, 2014)))

#Create the condition boolean series
condition = df_can['Continent']=='Asia'
print(condition)
print(df_can[condition])

#We can pass mutliple criteria in the same line.
print(df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')])

#The table as it is now
print('data dimensions:', df_can.shape)
print(df_can.columns)
print(df_can.head(2))

print("="*30)
haiti = df_can.loc['Haiti', years] # Passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

#Imigratin to Canada by Haiti
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(20, 6000, '2010 Earthquake')
plt.show()

#Immigrants from China and India
df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()
df_CI = df_CI.transpose()

df_CI.plot(kind='line')
plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

# inplace = True paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
# get the top 5 entries
df_top5 = df_can.head(5)
# transpose the dataframe
df_top5 = df_top5[years].transpose()
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
