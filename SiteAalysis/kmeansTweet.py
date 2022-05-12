import pandas as pd
import folium
map = folium.Map(tiles='cartodbpositron', location=[22.3529808, 114.107615], zoom_start=12)
LD_tweets = pd.read_csv("twitterdata.csv")
# add markers to the map to show the districts
markers_colors = []
for lat, lon, poi in zip(LD_tweets['latitude'], LD_tweets['longitude'], LD_tweets['District']):
    label = folium.Popup(str(poi))
    folium.CircleMarker(
        [lat, lon],
        radius=10,
        popup=label,
        fill=True,
        fill_color='#FFFFFF',
        fill_opacity=0.7).add_to(map)
       
map.save('ld-tweets.html')
display(IFrame('ld-tweets.html', width = 1500, height = 1200))
