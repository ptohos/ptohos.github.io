#!/usr/bin/python3
'''
 projectile shot with air resitance (drag force)
'''
import numpy as np
import matplotlib.pyplot as plt

# Define initial conditions and time step
v0    = 700 # m/s
dt    = 0.25 # s
#theta =55*(np.pi/180) # convert degrees to radians
theta = 55*(np.pi/180) # convert degrees to radians
A_m   = 4E-5 # drag coefficient
vx    = v0*np.cos(theta)
vy    = v0*np.sin(theta)

# Define variables
xList, yList = [],[]
xList.append(0)    # initial x-position
yList.append(0)    # initial y-position
xpos  = 0
ypos  = 0
n     = 0
g     = 9.81

# Infinite loop
while 1:
    # Define the force due to air resistance (to be used for fx or fy)
    f  = A_m*np.sqrt(vx**2 + vy**2)
    fx = f * vx
    fy = f * vy
    
    # Apply Euler-Cromer method to predict velocities
    vy   = vy - (g + fy) * dt  # mass?
    vx   = vx - (fx) * dt      # mass?

    # Predict positions
    xpos = xpos + vx * dt
    ypos = ypos + vy * dt
    xList.append(xpos)
    yList.append(ypos)

    n += 1
    # Break the loop if object hits the ground (y-position becomes negative)
    if yList[n] <= 0:
        break
t = n*dt

# Linear interpolation (Grammiki paremvoli) to find x-position of fall (range of projectile)
slope     = ( yList[n]-yList[n-1])/(xList[n]-xList[n-1])
xList[n]  = xList[n-1] - yList[n-1]/slope
yList[n]  = 0
xRange    = xList[n]
print("Projectile range = %.1f meters" % (xRange) )

plt.figure()
plt.plot(xList, yList, "b-", label="Projectile motion in fluid")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axvline(x=xRange, color='r',linestyle='--', label="Range is %.01f m (dt = %0.1f s)" % (xRange, t))
plt.legend()#title="Results: ")
#plt.text(0.8*xRange, 10100.0, 'maximum range', fontsize=12, color="red")
plt.grid(True)
plt.show()
