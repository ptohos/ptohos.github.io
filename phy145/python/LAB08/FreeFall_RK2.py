#!/usr/bin/python3
#=======================
# Runge-Kutta 2nd order 
# Free Fall
#====================

import numpy as np
import matplotlib.pyplot as plt

g = 9.9
X0 = 0.0
V0 = 0.0
dt =2.00
tfinal = 100.
#arxikopoiisi twn pinakwn
t = np.arange(0.,tfinal+dt,dt)
npoints = len(t)
X = np.zeros(npoints)
V = np.zeros(npoints)
XExact = X0 + V0*t - 0.5*g*t**2
#===================
#Lusi Runge-Kutta 2
#===================
X[0] = X0
V[0] = V0

for i in range(npoints-):
    #upologismos tis taxititas sto meso tou diastimatos
    Vmid = V[i] - 0.5 * g * dt
    #xrisi tis taxytitas sto endiameso simeio gia
    #euresi tis thesis sto telos tou xronikou diastimatos
    X[i+1] = X[i] + Vmid * dt
    V[i+1] = V[i] - g * dt
#=================
# Plot the results
#=================
plt.figure()
plt.plot(t,X,'mo',label='RK-2')
plt.plot(t,XExact,'k',label='Exact')
plt.xlabel('t (s)')
plt.ylabel('X (m)')
plt.legend()
plt.show()
