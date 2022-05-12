import pandas as pd
import numpy as np
import geopandas
import geopy
from IPython.display import IFrame
import matplotlib.cm as cm
import matplotlib.colors as colors
import folium # map rendering library
from sklearn.cluster import KMeans

LD_flicker = pd.read_csv("flickr_photos_2019_2022.csv")
print(LD_flicker)

# create map, LD_tweets['text']
# set location that make Hong Kong at the centre of the web page
# set zoom_start = 12 for better visualization
map = folium.Map(tiles='cartodbpositron', location=[48.88614492, 2.225888888], zoom_start=20)

# add markers to the map to show the districts
markers_colors = []
for lat, lon, til, des in zip(LD_flicker['latitude'], LD_flicker['longitude'], LD_flicker['title'], LD_flicker['description']):
    label = folium.Popup(str(til)+str(des))
    folium.CircleMarker(
        [lat, lon],
        radius=6,
        popup=label,
        fill=True,
        fill_color='#FFFFFF',
        fill_opacity=0.7).add_to(map)
       
map.save('ld_flicker.html')

class Flicker:
    def __init__(self, lat, lon, tit, des, lab):
        self.lat = latitude
        self.lon = longitude
        self.tit = title
        self.des = description
        self.lab = label
LD_Flicker = []
with open("flickr_photos_2019_2022.csv",encoding='utf-8') as FlickerData:
    reader = csv.DictReader(FlickerData)
    for row in reader:
        lat = row['latitude']
        lon = row['longitude']
        tit = row['title']
        des = row['description']
        lab = til + '--' + '"' + des +'"' 
        LD_Flicker.append(Flicker(lat, lon, tit, des, lab))
flickerInfo = LD_Flicker[0:100]