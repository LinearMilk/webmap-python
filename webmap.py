import pandas
import folium

df = pandas.read_csv("Volcanoes.txt")


def get_colour(colour):
    if colour<1000:
        return 'green'
    elif 1000<= colour <3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[-33, 151.5], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanos")
lon = list(df.LON)
lat = list(df.LAT)
name = list(df.NAME)
location = list(df.LOCATION)
status = list(df.STATUS)
elev = list(df.ELEV)

for ln, lt, nm, lc, st, el in zip(lon, lat, name, location, status, elev):
    popup = nm + '\n' + lc + '\n' + st + '\n' + str(format(el, "0.0f"))
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=popup, fill_color=get_colour(el), color="grey", radius=6, fill_opacity=0.6 , angle=0, prefix='glyphicon'))

fg.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
                            style_function= lambda x : {'fillColor':'yellow'}))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")

print("success")
