import folium
import pandas

data = pandas.read_csv('App1/Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[38.58, -99.09], zoom_start=8, tiles='OpenStreetMap')

fg = folium.FeatureGroup(name='My Map')

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+'m', icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('App1/Map1.html')

