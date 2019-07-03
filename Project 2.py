import pandas as pd
import folium

'''
dataset = pd.read_csv('database.csv')
lon = list(dataset['Longitude'])
lat = list(dataset['Latitude'])
ele = list(dataset['Elevation (Meters)'])

def magnitude(elevation):
    if elevation<1000:
        return 'green'
    elif 2000<elevation<4000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[30,-99],zoom_start=1,tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='Volcanoes')

for la,lo,el in zip(lat,lon,ele):
    if el<1000:
        fg.add_child(folium.Marker(location=[la,lo],popup=str(el)+'m', icon=folium.Icon(color=magnitude(el))))

map.add_child(fg)
map.save('folium.html')
#the above code points on the map the various volcanic activities seperated based on their magnitude
'''

'''
map = folium.Map(location=[30,77],zoom_start=8,tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='Children')

for coordinate in [[31.23,77.54],[32,78]]:
    fg.add_child(folium.Marker(location=[coordinate[0],coordinate[1]],popup='Child_1', icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save('folium.html')

#this marks locations on map as the child of the feature group
'''

#map.save('folium.html') #creates a file with the specified name containing the map