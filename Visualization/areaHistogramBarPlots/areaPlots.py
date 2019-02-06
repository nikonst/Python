import pandas as pd
import matplotlib.pyplot as plt

df_can = pd.read_excel('../Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print('Data downloaded and read into a dataframe!')
#Print the dimensions of the dataframe
print(df_can.shape)

#Clean up
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
#The first five elements and see how the dataframe was changed
print(df_can.head())

#Rename some of the columns so that they make sense.
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
#View the first five elements and see how the dataframe was changed
print(df_can.head())

#For consistency, ensure that all column labels of type string.
#Let's examine the types of the column labels
print(all(isinstance(column, str) for column in df_can.columns))

df_can.columns = list(map(str, df_can.columns))
#Check the column labels types now
print(all(isinstance(column, str) for column in df_can.columns))

#Set the country name as index - useful for quickly looking up countries using .loc method.
df_can.set_index('Country', inplace=True)
#View the first five elements and see how the dataframe was changed
print(df_can.head())

#Add total column.
df_can['Total'] = df_can.sum(axis=1)
print(df_can.head())
print ('data dimensions:', df_can.shape)
#List of years from 1980 - 2014
#This will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))
print(years)


# AREA PLOTS *******************************************************
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)
# transpose the dataframe
df_top5 = df_top5[years].transpose()
print(df_top5.head())

df_top5.plot(kind='area',
             stacked=False,
                alpha=0.35,
             figsize=(20, 9), # pass a tuple (x, y) size
            )
#Option 1: Scripting layer (procedural method) - using matplotlib.pyplot as 'plt'
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
#plt.show()
plt.savefig('areaPlots/areaPlot1.png')

#Option 2: Artist layer (Object oriented method) - using an Axes instance from Matplotlib (preferred)
ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 9)) #Stacked
ax.set_title('Immigration Trend of Top 5 Countries Ver 2')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')
#plt.show()
plt.savefig('areaPlots/areaPlot2.png')
