import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


print ('Matplotlib version: ', mpl.__version__ )

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

#BAR CHARTS *******************************************************
# step 1: get the data
df_iceland = df_can.loc['Iceland', years]
df_iceland.head()
# step 2: plot data
df_iceland.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot
#plt.show()
plt.savefig('barPlots/barPlot1.png')

#Add Text Effect on Bar Chart
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
# Annotate arrow
plt.annotate('',                      # s: str. Will leave it blank for no text
             xy=(32, 70),             # place head of the arrow at point (year 2012 , pop 70 )
             xytext=(28, 20),         # place base of the arrow at point (year 2008 , pop 20 )
             xycoords='data',         # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )
# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis', # text to display
             xy=(28,30),                   # start the text at at point (year 2008 , pop 30)
             rotation=72.5,                # Based on trial and error to match the arrow
             va='bottom',                  # Want the text to be vertically 'bottom' aligned
             ha='left',                    # Want the text to be horizontally 'left' algned.
            )
#plt.show()
plt.savefig('barPlots/barPlot2.png')

