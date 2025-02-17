import folium
map = folium.Map(location=[38.950817, -5.867413], zoom_start=13, tiles='OpenStreetMap')

fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[38.9508, -5.8674], popup="Hola soy el marker!", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('App1/Map1.html')

