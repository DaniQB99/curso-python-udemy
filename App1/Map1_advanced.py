import folium
import pandas
 
data = pandas.read_csv("App1/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html =  """
        Volcano name:
            <br>
                <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
            <br>
            Height: %s m
        """
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="OpenStreetMap")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("App1/Map_html_popup_advanced.html")