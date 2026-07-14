import kagglehub
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
import numpy as np
from matplotlib import pyplot as plt
import xyzservices.providers as xyz

# Download latest version
path = kagglehub.dataset_download("imdevskp/corona-virus-report")

print("Path to dataset files:", path)

