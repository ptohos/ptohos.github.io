#!/usr/bin/python3

import numpy as np
from random import random, seed

ZoneTemp=[30, 28, 23, 25, 20, 16, 11, 5, -5]

NMC = int(input("How many MC points for integration? "))
seed(12345)

RandomZone = [0 for x in range(len(ZoneTemp))]
R = 1
point_on_surface = 0

for itry in range(NMC):
    x = random()
    y = random()
    z = random()
    random_point = x*x + y*y + z*z
    if np.abs(random_point - R**2) <= 0.01 :
        point_on_surface += 1
        angle = np.arcsin(z/R)       # Find the zone it falls in
        angle = angle * 180.0/np.pi
        zone = int(angle/10)
        if zone >= len(ZoneTemp)-1: zone = 8
        RandomZone[zone] += 1        # Increment the total falling on this zone

ZoneArea, Error = [],[]
AveTemp = 0
for izone in range(len(ZoneTemp)):
    ZoneArea += [RandomZone[izone]/point_on_surface]
    Error += [np.sqrt(ZoneArea[izone]/RandomZone[izone])]

print('Total number of points generated on the surface: ',point_on_surface)
print(28*' ','Summary for zones')
print(' Low angle',5*'','Upper angle', 5*'','Sim. Fractional Area', \
        8*'','Sfalma',8*'','Theor. Fraction')

for izone in range(len(ZoneTemp)):
    Theor = np.sin((izone+1)*10*np.pi/180) - np.sin(izone*10*np.pi/180)
    print(' %4.0f %12.0f %20.5f %14.5f %11.5f'% \
          (izone,izone+1,ZoneArea[izone],Error[izone],Theor))
    AveTemp += ZoneTemp[izone] * ZoneArea[izone]

print('Average Temperature of the Earth = %10.4f'%AveTemp)


    
