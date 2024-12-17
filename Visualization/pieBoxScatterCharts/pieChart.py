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

#Years that we will be using in this lesson - useful for plotting later on
years = list(map(str, range(1980, 2014)))
print('data dimensions:', df_can.shape)

#Group countries by continents and apply sum() function
df_continents = df_can.groupby('Continent', axis=0).sum()

#note: the output of the groupby method is a `groupby' object.
#We can not use it further until we apply a function (eg .sum())
print(type(df_can.groupby('Continent', axis=0)))

print(df_continents.head())

# autopct create %, start angle represent starting point
df_continents['Total'].plot(kind='pie',
                            figsize=(5, 6),
                            autopct='%1.1f%%', # add in percentages
                            startangle=90,     # start angle 90° (Africa)
                            shadow=True,       # add shadow
                            )
plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.
#plt.show()
plt.savefig('pieCharts/pie1.png')

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.
df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )
# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12)
plt.axis('equal')
# add legend
plt.legend(labels=df_continents.index, loc='upper left')
#plt.show()
plt.savefig('pieCharts/pie2.png')