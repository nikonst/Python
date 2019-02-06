import pandas as pd
import folium
from folium import CircleMarker
#from folium import MarkerCluster


print("Folium Version:",folium.__version__)

# define the world map
world_map = folium.Map()
print(world_map)
world_map.save('foliumIntro/world_map.html')

# define the world map centered around Canada with a higher zoom level
world_map_canada = folium.Map(location=[56.130, -106.35], zoom_start=4)
world_map_canada.save('foliumIntro/world_map_canada.html')

# create a Stamen Toner map of the world centered around Canada
world_map_canada_toner = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')
world_map_canada_toner.save('foliumIntro/world_map_canada_toner.html')

# create a Stamen Terrain map of the world centered around Canada
world_map_canada_terrain= folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')
world_map_canada_terrain.save('foliumIntro/world_map_canada_terrain.html')

# create a world map with a Mapbox Bright style.
world_map_mapbox = folium.Map(tiles='Mapbox Bright')
world_map_mapbox.save('foliumIntro/world_map_mapbox.html')

df_incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
print('Dataset read into a pandas dataframe!')
print(df_incidents.head())
print(df_incidents.shape)
# get the first 1000 crimes in the df_incidents dataframe
limit = 1000
df_incidents = df_incidents.iloc[0:limit, :]
print(df_incidents.shape)
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
sanfran_map.save('foliumIntro/sanfran_map.html')

# Superimpose the locations of the crimes onto the map. The way to do that in Folium is to create a feature group
# with its own features and style and then add it to the sanfran_map.

# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 1000 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(

            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill_color='blue',
            fill_opacity=0.6
        )
    )
# add incidents to map
sanfran_map.add_child(incidents)

#You can also add some pop-up text that would get displayed when you hover over a marker.
# Let's make each marker display the category of the crime when hovered over.

# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 1000 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5,  # define how big you want the circle markers to be
            color='yellow',
            fill_color='blue',
            fill_opacity=0.6
        )
    )
# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)
for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)
# add incidents to map
sanfran_map.add_child(incidents)

'''

MarkerCluster() won't work


# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location = [latitude, longitude], zoom_start = 12)
# instantiate a mark cluster object for the incidents in the dataframe
incidents = folium.MarkerCluster().add_to(sanfran_map)
# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)
    
    '''

# display map
sanfran_map.save('foliumIntro/sanfran_map2.html')


