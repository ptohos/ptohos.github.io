#!/usr/bin/python3
#====================
# Plagia voli me
# antistasi aera 
#====================

import numpy as np
import matplotlib.pyplot as plt

dt =0.25
v0 = 700
theta = 55*np.pi/180
A_m = 4E-5
x, y = [],[]
x.append(0)    # arxiki x-thesi
y.append(0)    # arxiki y-thesi
xpos = 0
ypos = 0
vx = v0*np.cos(theta)
vy = v0*np.sin(theta)
istep = 0
doit = True

while doit:
    f = A_m*np.sqrt(vx**2 + vy**2)   # Antistasi tou aera
    vy = vy - 9.8 * dt - f * vy * dt
    vx = vx - f * vx * dt
    xpos = xpos + vx * dt
    ypos = ypos + vy * dt
    x.append(xpos)
    y.append(ypos)
    istep = istep + 1
    if y[istep] <= 0:
        doit = False

#Grammiki paremvoli gia euresi tis x-thesis ptwsis
nstep = istep
slope = (y[nstep]-y[nstep-1])/(x[nstep]-x[nstep-1])
x[nstep] = x[nstep-1] - y[nstep-1]/slope
y[nstep] = 0

plt.figure()
plt.plot(x,y)
plt.xlabel('ts')
plt.ylabel('y(m)')
plt.show()
