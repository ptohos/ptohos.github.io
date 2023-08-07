#!/usr/bin/python3

#=========================================================
#... To programma ayto lynei tis eksiswseis
#... kinisis tou aplou armonikou talantwnti
#... xrisimopoiwntas ti methodo
#...
#... Taxytitas Verlet
#=========================================================
import numpy as np
import matplotlib.pyplot as plt
#
def D1x(vx):
    dx = vx
    return dx

def D2x(x):
    dv = -(kspring/mass) * x
    return dv

def VelocityVerlet(xp,vp,ti,dt):
    xnew = xp + vp * dt + D1x(xp)*(dt*dt)/2
    vnew = vp + (D2x(xp) + D2x(xnew))*dt/2
    
    return xnew, vnew

t0 = float(input("Insert the initial time [t0]: "))
x0 = float(input("Insert the initial position [x0]: "))
v0 = float(input("Insert the initial velocityuu [v0]: "))
#
ntsteps = int(input("Insert the number of time steps: "))
ntime_mx= int(input("Insert the maximum time interval [number of periods]: "))
#
kspring = float(input("Spring constant: "))
mass = float(input("Mass of the body: "))
#
x = x0
v = v0
t = t0
#
# Energy of the system (potential + kinetic)
# Total mechanical energy should be conserved
#=============================================
E0 = 0.5*kspring*x**2 + 0.5*mass*v0**2

period = 2*np.pi*np.sqrt(kspring/mass)
tmax   = period * ntime_mx
dt     = tmax/ntsteps
time, xpos, velo, Ene = [], [], [], []
ipos = 0
#==============================
# Time evolution of the system
#==============================
while t <= tmax :
    E = 0.5 * mass * v**2 + 0.5 * kspring * x**2
    xpos +=[x]
    velo +=[v]
    Ene  +=[E]
    time +=[t]
    x, v =VelocityVerlet(xpos[ipos],velo[ipos],t,dt)
    ipos +=1
    t = t+dt
    
xpos = np.array(xpos)
velo = np.array(velo)
plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(time,xpos,'b-',)
plt.xlabel('time t(sec)')
plt.ylabel('position (m)')
plt.subplot(2,1,2)
plt.plot(time,Ene,'k-',label=r'$E_{mech}$')
plt.plot(time,0.5*kspring*xpos**2,'r-.',label=r'$E_{el}$')
plt.plot(time,0.5*mass*velo**2,'g:', label=r'$E_{kin}$')
plt.xlabel('time t(sec)')
plt.ylabel('Energy (Joule)')
plt.legend()

plt.tight_layout()
plt.show()
