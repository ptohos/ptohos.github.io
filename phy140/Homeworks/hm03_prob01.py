#!/usr/bin/python3

from math import pi

r = 10.6
a = 1.3    # one side of the rectangle

circle_area  = pi * r**2

b = 0      # a starting value for the unknow side of the rectangle
while a*b < circle_area:
    b += 1
b -= 1     # reduce the last value by 1 because te current value makes the area
           # of the rectangle larger than the area of the circle
print("The largest possible value of the side b of the rectangle is %3dcm"%b)
