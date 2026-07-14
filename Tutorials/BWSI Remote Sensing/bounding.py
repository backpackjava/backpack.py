import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon
from shapely import plotting

def getBoundingRectangle(poly):
  """
  input: poly, Polygon - any valid shapely Polygon object
  output: rect, Polygon - the minimum bounding upright rectangle
  Also plot the input Polygon as well as the bounding rectangle itself
  """
  min_x, min_y, max_x, max_y = poly.bounds
  rect = Polygon((min_x, min_y), ())
  
  pass


sample_poly = Polygon([(-100, -50), (-80, 90), (70, 80), (60, -60)])

# Get bounding rectangle
rect = getBoundingRectangle(sample_poly)

# Create matplotlib figure and axis
fig, ax = plt.subplots()

# Add original polygon
patch1 = shapely.plotting.patch_from_polygon(sample_poly, facecolor='#0000FF', edgecolor='black', alpha=0.5)
ax.add_patch(patch1)

# Add bounding rectangle
patch2 = shapely.plotting.patch_from_polygon(rect, facecolor='none', edgecolor='red', linewidth=2)
ax.add_patch(patch2)

# Add legend
handles = [plt.Line2D([0], [0], color="#5C5C81", lw=4),
           plt.Line2D([0], [0], color='red', lw=4)]
labels = ['Original Polygon', 'Bounding Rectangle']
ax.legend(handles, labels, loc='upper right')

# Move legend outside the plot so it does not cover the shape
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1.02, 0.5))

# Set plot limits and formatting
ax.set_xlim([-200, 200])
ax.set_ylim([-110, 110])
ax.set_aspect('equal')
plt.title("Polygon and Its Bounding Rectangle")
plt.grid(True)
plt.show()