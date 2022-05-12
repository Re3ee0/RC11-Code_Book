import pandas as pd
import numpy as np
import geopandas
import geopy
import requests
from IPython.display import IFrame
import matplotlib.cm as cm
import matplotlib.colors as colors
import folium # map rendering library
from sklearn.cluster import KMeans
import shapely.geometry
import pyproj
import csv

#Strait of the real limit
Smin_lng = 2.225684
Smin_lat = 48.885438
Smax_lng = 2.253922
Smax_lat = 48.897599

#number of cubes in two dimension
lng_count = 20
lat_count = 13

#get each step of two dimension
delta_lng = Smax_lng - Smin_lng
delta_lat = Smax_lat - Smin_lat

step_lng = delta_lng/lng_count
step_lat = delta_lat/lat_count

min_lng = Smin_lng + step_lng/2
min_lat = Smin_lat + step_lat/2
max_lng = Smax_lng - step_lng/2
max_lat = Smax_lat - step_lat/2

print(min_lng,min_lat,max_lng,max_lat)

gridpoints = []
y = min_lat
while y < max_lat:
    x = min_lng
    while x < max_lng:
        p = (x,y)
        gridpoints.append(p)
        y += step_lat
    x += step_lng  

with open('grid.csv', 'w') as of:
    of.write('longitude,latitude\n')
    for p in gridpoints:
        of.write('{}\n'.format(str(p)))