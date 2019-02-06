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
df_japan = df_can.loc[['Japan'], years].transpose()
print(df_japan.head())
df_japan.describe()

df_japan.plot(kind='box', figsize=(8, 6))
plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')
#plt.show()
plt.savefig('boxPlots/box1.png')

#--------------------------------------------------------------------------------------------------------
#Compare the distribution of the number of new immigrants from India and China for the period 1980 - 2013.

df_CI= df_can.ix[['China', 'India'], years].transpose() # recall .ix is another alternative to .loc and .iloc

print(df_CI.head())
df_CI.describe()

df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)
plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')
#plt.show()
plt.savefig('boxPlots/box2.png')

#Subplots
fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(122) # add subplot 2 (1 row, 2 columns, second plot).

# Subplot 1: Box plot
df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_CI.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')
#plt.show()
plt.savefig('boxPlots/box3.png')

#Create a box plot to visualize the distribution of the top 15 countries
# (based on total immigration) grouped by the decades 1980s, 1990s, and 2000s.

# 1. get the top 15 countries based on Total immigrant population
df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)
#df_top15

# 2. create a new dataframe which contains the aggregate for each decade
#Get a list of all years in decades 80's and 90's
years_80s = list(map(str, range(1980, 1990)))
years_90s = list(map(str, range(1990, 2000)))
years_00s = list(map(str, range(2000, 2010)))
#Slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1)
df_90s = df_top15.loc[:, years_90s].sum(axis=1)
df_00s = df_top15.loc[:, years_00s].sum(axis=1)
#Merge the two series into a new data frame
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s':df_00s})
print(new_df)
new_df.describe()

new_df.plot(kind='box', figsize=(10, 6))
plt.title('Immigration from top 15 countries for decades 80s, 90s and 2000s')
#plt.show()
plt.savefig('boxPlots/box4.png')

