import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
from shapely import plotting
from shapely.affinity import affine_transform, rotate, skew, scale, translate

forecast1 = Point(0,0).buffer(0.3)
forecast2 = Point(-1,1.3).buffer(0.5)
forecast3 = Point(-2.2,2.4).buffer(1)
forecast4 = Point(-2.5,4.6).buffer(1.5)
forecast5 = Point(-1,8.1).buffer(2.2)
forecast6 = Point(3,8.5).buffer(2.6)

all_forecasts = MultiPolygon([forecast1,
                              forecast2,
                              forecast3,
                              forecast4,
                              forecast5,
                              forecast6]).convex_hull

all_forecasts2 = shapely.union_all(MultiPolygon([forecast1,
                              forecast2,
                              forecast3,
                              forecast4,
                              forecast5,
                              forecast6]))
fig = plt.figure()
ax1 = fig.add_subplot(111)

patch = shapely.plotting.patch_from_polygon(all_forecasts, 
                                            facecolor="#1223B8", 
                                            edgecolor='black', alpha=0.5, 
                                            linewidth=1)
patch2 = shapely.plotting.patch_from_polygon(all_forecasts2, 
                                             facecolor="#00DA1D", 
                                             edgecolor='black', alpha=0.5, 
                                             linewidth=1)

minX,minY,maxX,maxY = all_forecasts.bounds

ax1.set_xlim([minX, maxX])
ax1.set_ylim([minY, maxY])

ax1.add_patch(patch)
ax1.add_patch(patch2)

plt.show()