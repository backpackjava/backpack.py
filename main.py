import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import numpy as np
from matplotlib import pyplot as plt
import xyzservices.providers as xyz

file_path = "C:/Users/rad11/Python Projects VSCode/backpack.py/phl_ica_floodrisk_geonode_mar2014.zip"
data = gpd.read_file(file_path)
data_proj = data.to_crs(epsg=3857)
# print(data.head())
# print(data.bounds) #data.boundary

# print(data.crs.axis_info)

# data_crs_3857 = data.to_crs(3857)
# print(data_crs_3857.crs)

# DO THE EXERCISE ON AREA LATER~! REVIEW SHAPELY LATER~!

newdata = gpd.GeoDataFrame(geometry=gpd.GeoSeries())

coordinates = [(-71.092562, 42.357602), ( -71.080155, 42.361553), ( -71.089817, 42.362584), (-71.094688, 42.360198)]
poly = Polygon(coordinates)

newdata.loc[0, 'geometry'] = poly
newdata['location'] = gpd.pd.Series(dtype='object')
newdata.loc[0, 'location'] = 'MIT main campus'

newdata = newdata.set_crs('epsg:4326')

newdata.to_file("output_data/MIT_campus.shp")

ax = newdata.to_crs(epsg=3857).plot(figsize=(10,5),alpha = 0.5, color='#FF55FF')
ctx.add_basemap(ax)
ax.set_axis_off() # remove the x-y axes
plt.savefig('MIT_main_campus_poly.png')

print(newdata)