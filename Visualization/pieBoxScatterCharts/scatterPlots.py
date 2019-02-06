import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_can = pd.read_excel('../Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print(df_can.head())
print(df_can.shape)

#Clean up the data set to remove unnecessary columns (eg. REG)
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

#Rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

#For sake of consistency, make all column labels of type string
df_can.columns = list(map(str, df_can.columns))

#Set the country name as index - useful for quickly looking up countries using .loc method
df_can.set_index('Country', inplace=True)

#Add total column
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float,df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')
plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
#plt.show()
plt.savefig('scatterPlots/scatter1.png')

#**************************************************************************************
#Plot a linear line of best fit, and use it to predict the number of immigrants in 2015.

x = df_tot.year      # year on x-axis
y = df_tot.total     # total on y-axis
fit = np.polyfit(x, y, deg=1)

print(fit)

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plot line of best fit
plt.plot(x,fit[0]*x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))
#plt.show()
plt.savefig('scatterPlots/scatter2.png')

# Print out the line of best fit
'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1])

#**************************************************************************************
#Plot a bubble plot of immigration from Brazil and Argentina for the years 1980 - 2013.
#Set the weights for the bubble as the normalized value of the population for each year

df_can_t=df_can[years].transpose() # transposed dataframe
#Cast the Years (the index) to type float
df_can_t.index = map(float,df_can_t.index)
#Let us label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = 'Year'
#Reset index to bring the Year in as a column
df_can_t.reset_index(inplace = True)
#View the changes
df_can_t.head(3)

norm_brazil = (df_can_t.Brazil - df_can_t.Brazil.min()) / (df_can_t.Brazil.max() - df_can_t.Brazil.min())
norm_argentina = (df_can_t.Argentina - df_can_t.Argentina.min()) / (df_can_t.Argentina.max() - df_can_t.Argentina.min())
print(norm_brazil)

# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(14, 8),
                    alpha=0.5,                  # transparency
                    color='green',
                    s=norm_brazil * 2000 + 10,  # pass in weights
                    xlim=(1975, 2015)
                   )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 2000 + 10,
                    ax = ax0
                   )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 - 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')

#plt.show()
plt.savefig('scatterPlots/scatter3.png')