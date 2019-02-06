import numpy as np
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

# HISTOGRAMS *******************************************************
print(df_can['2013'].head())

# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can['2013'])
print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins

df_can['2013'].plot(kind='hist', figsize=(8, 5))
plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
#plt.show()
plt.savefig('histogramPlots/hist1.png')

# 'bin_edges' is a list of bin intervals
count, bin_edges = np.histogram(df_can['2013'])
df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)
plt.title('Histogram of Immigration from 195 countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
#plt.show()
plt.savefig('histogramPlots/hist2.png')

#What is the immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013?

#View the data set
df_can.loc[['Denmark', 'Norway', 'Sweden'], years]
#Generate histogram
df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()

#Transpose dataframe
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_t.head()

#Generate histogram
df_t.plot(kind='hist', figsize=(10, 6))
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
#plt.show()
plt.savefig('histogramPlots/hist3.png')

'''
Let us make a few modifications to improve the impact and aesthetics of the previous plot:

    increase the bin size to 15 by passing in bins parameter
    set transparency to 60% by passing in alpha paramemter
    label the x-axis by passing in x-label paramater
    change the colors of the plots by passing in color parameter
'''
# Let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)
# Un-stacked Histogram
df_t.plot(kind ='hist',
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
#plt.show()
plt.savefig('histogramPlots/hist4.png')

'''
If we do no want the plots to overlap each other, we can stack them using the stacked paramemter.
Let us also adjust the min and max x-axis labels to remove the extra gap on the edges of the plot.
We can pass a tuple (min,max) using the xlim paramater, as show below.
'''

count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

#Stacked Histogram
df_t.plot(kind='hist',
          figsize=(10, 6),
          bins=15,
          xticks=bin_edges,
          color=['coral','darkslateblue','mediumseagreen'],
          stacked=True,
          xlim=(xmin,xmax)
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
#plt.show()
plt.savefig('histogramPlots/hist5.png')