#!/usr/bin/python3
#==========================
# Efarmog;i methodo Euler
# se radienergi diaspasi
#===========================
import numpy as np
import math
import matplotlib.pyplot as plt

# set parameters
k = 0.05
N0 = 1000.
dt = 2.
tfinal = 100.

# initialize array of time t
t = np.arange(0.,tfinal+dt,dt)
t = [k*dt for k in range(int((tfinal+dt)/dt))]
npoints = len(t)

# initialize tis listes for solution
NExact = [] ; N = []
NExact = [N0 * np.exp(-k*time) for time in t] # compute exact solution for comparison

# Euler Solution
N += [N0]
for i in range(npoints-1):
    N += [N[i] - k * N[i] * dt]

# Plot results
plt.figure(1)
plt.plot(t,N,'mo',label='Euler')
plt.plot(t,NExact,'k',label='Exact')
plt.xlabel('t')
plt.ylabel('N')
plt.legend()
plt.axis([-5,105,-10,1010])
plt.grid('on')
#====================
# The error
#====================
NDiff = [ (N[i]-NExact[i]) for i in range(len(N))]
plt.figure(2)
plt.plot(t,NDiff,'bo')
plt.xlabel('t')
plt.ylabel('Euler - Exact')
plt.axis([-5,105,-20,1])
plt.grid('on')
plt.show()
