import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point32D = Point(9.26, -2.456,0)

line = LineString([point1,point2,point3])
identical_line = LineString([(2.2,4.2),(7.2,-25.1),(9.26, -2.456)])
# line by either a list of points or list of ordered tuples

line_Coords = line.coords
print(line.coords[0]) # 0th point in the line
print(line.coords[0][0]) # x-value of 0th point in the line

length = line.length
centroid = line.centroid

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1) # row, column, which column

ax1.plot(line)
ax1.plot(centroid)
plt.show() 

line2 = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1)])

def getMidpoint(line):
    length = line.length
    to_interp = length/2
    return(line.interpolate(to_interp))

print(getMidpoint(line2))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x, y = line2.xy
ax1.plot(x, y, marker = "*", color = 'blue')
ax1.plot(getMidpoint(line2).coords[0][0], getMidpoint(line2).coords[0][1], marker = "o", color = 'orange')
plt.show()