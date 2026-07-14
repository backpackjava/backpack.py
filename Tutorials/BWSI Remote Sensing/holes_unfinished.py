import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon
from shapely import plotting

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

poly_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
single_hole = [[(170, 80), (170, -80), (-170, -80), (-170, 80)]]
double_hole = [[(100, 80), (100, -80), (-10, -20), (-10, 20)],[(-20, 30),(-125, -45),(-120, 40)]]

patch = shapely.plotting.patch_from_polygon(poly, facecolor='#FF6600', edgecolor='black', alpha=0.5, linewidth=1)
ax1.add_patch(patch)

x_min, y_min, x_max, y_max = poly.bounds
ax1.set_xlim([x_min, x_max])
ax1.set_ylim([y_min, y_max])

plt.show()