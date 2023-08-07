#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

g, dt = 9.8, 0.02   #g and time step
y, v0 = 0.0, 5.0    #arxiki thesi kai taxutita

ta,ya = [],[]
t, yb = [],[]

v = v0
while t< 1.0:       #ekseliksi tou sustimatos gia 1s
    ta.append(t)
    ya.append(y)
    yb.append(v0*t - g*t*t/2.0)   # Theoritiki lusi

    y = y + v*dt   #Euler vima gia ti thesi 
    v = v - g*dt   #Euler vima gia tin taxutita
    t = t + dt

plt.figure
plt.plot(ta,ya,ta,yb,'--')
plt.xlabel('ts')
plt.ylabel('y(m)')
plt.show()
