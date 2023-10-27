#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def interpolate(pos1,PosI,PosF):
    slope = (PosF[1] - PosI[1])/(PosF[0] - PosI[0])
    pos2 = PosI[1] + slope * (pos1 - PosI[0])
    return pos2

#====================
# Initial conditions
#====================
x0 = float(input("Insert the initial x-position of the object "))
y0 = float(input("Insert the initial y-position of the object "))
v0 = float(input("Insert the initial velocity of the object "))
theta0 = float(input("Insert the initial angle with respect to horizon "))
t0 = float(input("Insert the initial time "))
dt = float(input("Insert the time step "))
accel = -9.81
theta = theta0*np.pi/180
v0x   = v0*np.cos(theta)
v0y   = v0*np.sin(theta)

t = t0      # Initial time
x = []      # x-position list
y = []      # y-position lists
time=[]     # time array
x += [x0]   # initial position  - append tin arxiki timi
y += [y0]   # Initial position  - append tin arxiki timi
time+=[t0]
ist = 0
while y[ist] >= 0 or t == 0:
    ist  += 1
    t    += 0.1
    time += [t]
    x    += [x0 + v0x * t] 
    y    += [y0 + v0y * t + 0.5*accel*t*t]
xlast  = x[ist]
xblast = x[ist-1]
ylast  = y[ist]
yblast = y[ist-1]
tlast  = time[ist]
tblast = time[ist-1]
r0pos=np.zeros(2)
r1pos=np.zeros(2)
r0pos[0] = yblast
r0pos[1] = xblast
r1pos[0] = ylast
r1pos[1] = xlast
yfin = 0
xfin = interpolate(yfin,r0pos,r1pos)
tfin = xfin/v0x
y[ist] = yfin
x[ist] = xfin
print(f'The projectile range is {xfin:5.2f}m')
print(f'The time of flight is {tfin:5.2f}s')
# Use the range to find the time of flight
#===========================================
r0pos[0] = time[ist-1]
r0pos[1] = x[ist-1]
r1pos[0] = time[ist]
r1pos[1] = x[ist]


plt.figure(figsize=(5,5))
plt.plot(x,y,'b-',lw=2)
plt.title('projectile trajectory')
plt.xlim(0,70)
plt.ylim(0,35)
plt.xlabel('x - position (m)')
plt.ylabel('y - position (m)')
plt.text(42,33,r'Initial position (0,25)')
plt.text(42,31,r'$\upsilon_0 = 22m/s$')
plt.text(42,29,r'$\theta_0 = 30^o$')
plt.text(42,27,rf'Range = {xfin:5.2f}m')
plt.text(42,25,rf'Flight time = {tfin:5.2f}s')
plt.axhline(y=25,color='red',linestyle='--')
plt.savefig('Trajectory.pdf')
plt.show()


    
