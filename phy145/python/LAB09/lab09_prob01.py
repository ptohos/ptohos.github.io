#!/usr/bin/python3

#========================================
#...To programma vriskei tis eksiswseis
#...kinisis enos vlimatos xrisimipoiontas
#...ti methodo velocity_verlet
#...
#...Symfwna me ti methodo ayti tha prepei
#...na lusoume tis eksiswseis:
#... u_n+1 = u_n + dt/2*(a_n + a_n+1)
#... r_n+1 = r_n + dt*u_n + a_n*dt**2/2 
#... Sti periptwsi tou provlimatos mas
#... H epitaxynsi sti y dieythynsi einai
#... pantote statheri kai isi me g
#... epomenws ay_n = ay_n+1 = g
#... Sti dieythunsi x den yparxei 
#... epitaxynsi opote oi eksiswseis 
#... aplopoiountai
#========================================
import numpy as np
import matplotlib.pyplot as plt

def init():
    vel = float(input("Insert the initial velocity: "))
    ang = float(input("Insert the angle of throw [degrees]: "))
    xo = float(input("Insert the initial x-position: "))
    yo = float(input("Insert the initial y-position: "))
    to = float(input("Insert the initial time: "))
    dt = float(input("Insert the time step: "))

    ang = ang*np.pi/180.
    return vel, ang, xo, yo, to, dt 


def accel(option, x, y, time):
    #=================================================
    #... Edw ousiastika prepei na exoume ti morfi tis
    #... dunamis pou prokalei ti synistwsa epitaxunsi
    #... se kathe dieythynsi. 
    #... H dunami ayti den einai aparaitita statheri
    #... alla mporei na metabaletai analoga me ti 
    #... thesi kai ti xroniki stigmi. 
    #... H epitaxunsi vrisketai profanws diairwntas 
    #... ti dynami me ti maza toy systimatos 
    #=================================================
    if option == 1:
        acceleration = 0.       # Epitaxunsi stin x-dieythunsi
    if option == 2:
        acceleration = g        # mono i dunami tis varititas
    return acceleration



g = -9.81   #m/s^2
v0,angle,x0,y0,t0,dt = init()
ux  = v0 * np.cos(angle)
uy  = v0 * np.sin(angle)
x   = x0
y   = y0
x_eu = x0
y_eu = y0
ux_eu = ux
uy_eu = uy
ax  = 0
ay  = g
time = t0
t, xpos, ypos = [],[],[]
velx, vely = [],[]
xpos_eu, ypos_eu = [], []
xthe, ythe = [], []

doit = True
while doit:
    t.append(time)
    xpos.append(x)
    ypos.append(y)
    
    #Analytical solution
    #====================
    xthe.append(x0 + v0*np.cos(angle)*time)                
    ythe.append(y0 + v0*np.sin(angle)*time + g*time*time/2)
    
    #Euler method
    #=============
    accelx = accel(1, x_eu, y_eu, time)
    accely = accel(2, x_eu, y_eu, time)
    x_eu = x_eu + ux_eu*dt
    y_eu = y_eu + uy_eu*dt
    ux_eu = ux_eu + accelx*dt
    uy_eu = uy_eu + accely*dt
    xpos_eu.append(x_eu)
    ypos_eu.append(y_eu)
    
    #Verlet-taxytitas
    #================
    x_old  = x
    y_old  = y
    ux_old = ux
    uy_old = uy
    ax_old = ax
    ay_old = ay
    
    y = y + uy_old*dt + ay_old*(dt*dt)/2
    x = x + ux_old*dt + ax_old*(dt*dt)/2

    ax = accel(1,x,y,time+dt)  # Ypologismos tis epitaxunsis sti thesi t+dt [a_n+1]
    ay = accel(2,x,y,time+dt)  # apo ti dunami i opoia eksartatai apo x kai y thesi

    uy = uy + 0.5 * (ay_old + ay) * dt
    ux = ux + 0.5 * (ax_old + ax) * dt

    time = time + dt
    if y <= 0:             # Kanonika gia na vroume ti swsti thesi tha prepei na
        doit = False       # efarmosoume linear interpolation


plt.figure(figsize=(7,5))
plt.plot(xthe,ythe,'k-', label='Analytical')
plt.plot(xpos, ypos, 'b:', label='Verlet')
plt.plot(xpos_eu, ypos_eu, 'r-.', label='Euler')
plt.legend()
plt.grid(True)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.show()
