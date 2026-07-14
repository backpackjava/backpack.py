import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
from shapely import plotting
from shapely.affinity import affine_transform, rotate, skew, scale, translate

outer_rect_corner_bl = Point(1,1)
outer_rect_corner_br = Point(6,1)
outer_rect_corner_tl = Point(1,1)
outer_rect_corner_tr = Point(6,7)

outer_rect = ([()])