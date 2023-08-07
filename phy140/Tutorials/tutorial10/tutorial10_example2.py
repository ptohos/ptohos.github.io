#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Define variables
g, dt = 9.81, 0.02    # g, time step
y, v0 = 0.0, 5.0      # initial position, initial velocity
tList, yList = [],[] # list to hold solutions using Euler's Method
yTheory = []  # list to hold theoretical solution (y = ut + 0.5 a t**2)
v = v0
t = 0.0

# Time evolution of the system until t = 1.0 seconds (dt/step = nSteps)
while t < 1.0:
    tList.append(t)
    yList.append(y)
    yTheory.append(v0*t - g*t*t/2.0)   # theoretical solution
    
    y = y + v*dt   #Euler step for position
    v = v - g*dt   #Euler step for velocity
    t = t + dt

plt.figure()
#plt.plot(tList, yList, tList, yTheory, '--', lw=2)
plt.plot(tList, yTheory, 'b-', lw=2, label="Exact solution")
plt.plot(tList, yList  , 'r--', lw=2, label="Euler's method")
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.legend(title="Parameters: ")
plt.show()
