#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

g  = 9.8  # gravitational acceleration
T0 = 0    # initial time
h0 = float(input("Give the initial height of the projectile "))
u0 = float(input("Give the magnitude of the initial velocity "))
Tol = float(input("Give the projectile's time of flight "))
timestep = float(input("Give the time step to study the motion "))

NumberOfIntervals = int((Tol - T0)/timestep) + 1
time = np.linspace(T0,Tol,NumberOfIntervals)

# Anti na xrisimopoiisoume ti sunartisi linspace tis numpy
# mporoume na to kanoume kai me list. Dokimaste to afou
# svisete ta sxolia stis epomenes 4 entoles
# def f(x):
#    return x*timestep
# atime= list(range(NumberOfIntervals))
# time = list(map(f,atime))

h = h0 + u0 * time - 0.5*g*(time)*(time) # Vectorization
u = u0 - g*time

plt.plot(time,h)    # Sto x-aksona o xronos kai ston y i thesi
plt.xlabel('t(s)')
plt.ylabel('h(m)')
plt.show()
