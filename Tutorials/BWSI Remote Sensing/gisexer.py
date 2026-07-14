import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import numpy as np
from matplotlib import pyplot as plt
import xyzservices.providers as xyz
import math

data = gpd.read_file("C:/Users/rad11/Downloads/tx_texas_zip_codes_geo.min.json")

data.to_crs(epsg=3857)
# print(data.crs)

# print(f"Smallest Zip Code Area: {min(data['geometry'].area)}")
# print(f"Smallest Zip Code Area: {max(data['geometry'].area)}")

data['water_percentage'] = data['AWATER10'] / (data['ALAND10'] + data['AWATER10'])
print(data)

ax = data.plot(column = 'water_percentage', cmap="viridis",legend=True)
ax = data.plot(column = 'ALAND10')
ctx.add_basemap(ax = ax,source=ctx.providers.CartoDB.Positron,zoom=7)
plt.show()



# map = data.explore(tiles=xyz.CartoDB.Voyager)
# map.show_in_browser()