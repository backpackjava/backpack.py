import shapely
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, LineString, Polygon

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3D = Point(9.26, -2.456,0.57)
point32D = Point(9.26, -2.456,0)

# print(point1)
# print(point3D)
# print(type(point1))
# print(type(point3D))

# point1_coords = point1.coords

# point1_xy = (point1_coords.xy)
# print(point1_xy)
print(point1.x)
print(point1.y)

# point_dist = point1.distance(point2)
# print(point_dist)

# def distance3D(pointUno, pointDos):
    # pointUnoCoords = pointUno.coords
    # pointDosXY = pointDos.coords.xy
    # distance3D = np.sqrt((pointDos.x - pointUno.x)**2 + (pointDos.y - pointUno.y)**2 + (pointDosXY[2] - pointUno[2])**2)
    # return(distance3D)

def getClosestDist(pointsList):
    pointsListAttr = pointsList
    distances = []
    used = []
    for i in range(len(pointsList)):
        for j in range(len(pointsList)):
            if i != j:
                distances.append(pointsList[i].distance(pointsList[j]))
    return(min(distances))

# print(getClosestDist([point1, point2, point3D]))

def getClosestDistWIndex(pointsList):
    to_return = []
    to_return.append(getClosestDist(pointsList))
    to_return.append()

