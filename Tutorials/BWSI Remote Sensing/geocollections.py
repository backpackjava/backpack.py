import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon
from shapely import plotting
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box

# geometry collections tosres multiple distinct geometric shapes /elements

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
multi_point2 = MultiPoint([point1, point2, point3])

line1 = LineString([point1, point2])
line2 = LineString([point1, point3])
multi_line = MultiLineString([line1, line2])

circle1 = Point(0,0).buffer(1)
circle2 = Point(2,5).buffer(5)
circle3 = Point(10,10).buffer(7)
circle4 = Point(10,11).buffer(3)
multi_circle = MultiPolygon([circle1,circle2,circle3,circle4])

