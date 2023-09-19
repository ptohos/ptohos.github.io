#!/usr/bin/python3

import numpy as np
import matplotlib as plot

h0 = float(input("Give the initial height of the projectile "))
u0 = float(input("Give the magnitude of the initial velocity "))
g = 9.8
time = float(input("Give the projectile's time of flight "))

h = h0 + u0 * time - 0.5*g*(time)*(time) # Panta kalutera na xrisimopoioume
                                       # aples prakseis anti dunamewn pou
                                       # stirizontai se sunartiseis vivliothikis
u = u0 - g*time

print("After time of ",time,"s")
print("the projectile is at a height of ", h, "m")
print("moving with a velocity of %7.3f m/s"%u)
