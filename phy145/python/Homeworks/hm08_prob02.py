#!/usr/bin/python3
'''===========================================
   To programm upologizei ti ropi adraneias
   enos diskou D aktinas R = 1 ws pros tyxaio
   simeio me syntetagmenes (xo,yo) me ti 
   methodo oloklirwsis MC. To kentro 
   tou diskou exei suntetagmenes (0,0)
   ===========================================''' 
import numpy as np
from random import seed, random

seed(123456)

radius = float(input("Enter the disk's radius [R = 1] "))
Ntries = int(input("Enter the number of MC tries "))

for i in range(3):
    sum = 0.0
    Npnts = 0
    xo,yo = input("Enter the coordinates of the reference point [xo,yo]").split(",")
    xo = float(xo)
    yo = float(yo)
    while Npnts < Ntries:
        x = radius * (2 * random() - 1.0)  # the random points should be in the 
        y = radius * (2 * random() - 1.0)  # orthogonal that encloses the disk
        if x**2 + y**2 < radius :
            Npnts += 1
            dx = x - xo
            dy = y - yo
            sum += (dx*dx + dy*dy)
            
    MomOfInertia = sum/Npnts
    print("H ropi adraneias tou diskou ws pros simeio (%3.1f,%3.1f) einai: %5.4f"%(xo,yo,MomOfInertia))
