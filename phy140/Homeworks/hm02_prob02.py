#!/usr/bin/python3

import numpy as np

PlanCoord = []
coord=[]
xcoord = input("Coordinates of 1st point [xcoord] ")
ycoord = input("Coordinates of 1st point [ycoord] ")
coord +=[float(xcoord)]
coord +=[float(ycoord)]
PlanCoord +=[coord]
coord=[]
xcoord = input("Coordinates of 1st point [xcoord] ")
ycoord = input("Coordinates of 1st point [ycoord] ")
coord +=[float(xcoord)]
coord +=[float(ycoord)]
PlanCoord +=[coord]

slope = -99.
try:
    delta_x = PlanCoord[0][0]-PlanCoord[1][0]
except:
    delta_x = 1E-6
    print("x coordinates of the two points are almost the same")
    
delta_y = PlanCoord[0][1]-PlanCoord[1][1]

slope = delta_y/delta_x
distance = np.sqrt(delta_x*delta_x + delta_y*delta_y)

print("Two points with coordinates (%.5f,%.5f) and (%.5f,%.5f) respectively"%
      (PlanCoord[0][0],PlanCoord[0][1],PlanCoord[1][0],PlanCoord[1][1]))
print("The slope of the line passing through these points is %.5f"%slope)
print("The distance of the two points is %.5f"%distance)

                                                                 
