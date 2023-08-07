#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


#====================
# Initial conditions
#====================

x0 = float(input("Insert the initial x-posotion of the object "))
y0 = float(input("Insert the initial y-position of the object "))
v0 = float(input("Insert the initial velocity of the object "))
theta0 = float(input("Insert the initial angle with respect to horizon "))
t0 = float(input("Insert the initial time "))
dt = float(input("Insert the time step "))
accel = -9.81
theta = theta0*np.pi/180
dt    = 0.1
v0x   = v0*np.cos(theta)
v0y   = v0*np.sin(theta)

t = t0      # Initial time
x = []      # x-position list
y = []      # y-position lists
x += [x0]   # initial position  - append tin arxiki timi
y += [y0]   # Initial position  - append tin arxiki timi
ist = 0
while y[ist] >= 0 or t == 0:
    ist += 1
    t   += 0.1
    x   += [x0 + v0x * t] 
    y   += [y0 + v0y * t + 0.5*accel*t*t]

plt.figure(figsize=(5,5))
plt.plot(x,y,'b-',lw=2)
plt.title('projectile trajectory')
plt.xlim(0,70)
plt.ylim(0,35)
plt.xlabel('x - position (m)')
plt.ylabel('y - position (m)')
plt.text(40,32,r'Initial position (0,25)')
plt.text(40,30,r'$\upsilon_0 = 22m/s$')
plt.text(40,28,r'$\theta_0 = 30^o$')

plt.axhline(y=25,color='red',linestyle='--')
plt.savefig('Trajectory.pdf')
plt.show()


    
