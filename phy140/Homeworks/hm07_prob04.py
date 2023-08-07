#!/usr/bin/python3

def Vary_g(y):
    G=6.67259E-11
    M=5.972E24
    R=6.37815E6
    return G*M/(R+y)**2

def VaryDensity(air0,ypos):
    h = 1E4
    return air0*np.exp(-(ypos)/h)
    
def Xaccel(ypos, xSpeed, ySpeed, VaryDens, air0, DragBM):
    density = 1
    if (VaryDens):
        density = VaryDensity(air0,ypos)
        density = density/air0

    accel = -density*DragBM*np.sqrt(xSpeed*xSpeed + ySpeed*ySpeed)*xSpeed
    return accel

def Yaccel(ypos, xSpeed, ySpeed, VaryG, VaryDens, air0, DragBM):

    g=9.81
    if VaryG:
        g=Vary_g(ypos)

    density = 1
    if (VaryDens):
        density = VaryDensity(air0,ypos)
        density = density/air0
        
    accel = -g - density*DragBM*np.sqrt(xSpeed*xSpeed+ySpeed*ySpeed)*ySpeed
    return accel

def interpolate(x0,x1,y0,y1,yfin):
    ''' Approximate with straight line a function of y vs x
    and estimate the coordinates of a point wbetween two known
    points of the curve as well as the other 2nd coordinate of the
    point.
    It is based on slope = (y1 - y0)/(x1 - x0) = (yfin - y0)/(xfin - x0)
    where we solve for xfin '''
    
    xfin = x0 + (x1 - x0)*(yfin - y0) / (y1 - y0)
    return xfin
    
def propagate(pos, vel, t0, tstep, g_flag, density_flag,air0,DragBM):
    x, y, t = [], [], []

    ux   = vel[0]
    uy   = vel[1]
    xpos = pos[0]
    ypos = pos[1]
    tpos = t0
    dt = tstep

    x += [xpos]   # Initial conditions
    y += [ypos]
    t += [tpos]
    istep=0
    doit=True

    VaryG = g_flag
    VaryDens = density_flag
    while doit:  
        u = np.sqrt((ux**2)+(uy**2))
        ax = Xaccel(ypos, ux, uy, VaryDens, air0, DragBM)   
        ay = Yaccel(ypos, ux, uy, VaryG, VaryDens, air0, DragBM)
        uy_prev = uy
        uy = uy + ay*dt          #<< Vima Euler
        ux = ux + ax*dt          #<< Vima Euler
        xpos = xpos + ux*dt      #<< Vima Euler-Cromer
        ypos = ypos + uy*dt      #<< Vima Euler-Cromer
        tpos = tpos + dt
        x += [xpos]
        y += [ypos]
        t += [tpos]
        istep=istep+1
        
        if (uy_prev * uy) <= 0 : #<< Allagi prosimou tis taxutitas
                                 #<< (megisto upsos)
            uy_hmax = 0
            ymax = interpolate(y[-2], y[-1], uy_prev, uy, uy_hmax)
            
        if ypos <= 0:
            doit=False 
            ypos_xmax = 0 
            xrange = interpolate(x[-2],x[-1],y[-2],y[-1],ypos_xmax)
            t_flight = interpolate(t[-2],t[-1],y[-2],y[-1],ypos_xmax)
    #
    x[-1] = xrange               # correct the range after the interpolation
    y[-1] = 0                    # back to the ground
    t[-1] = t_flight             # total time of flight 
    return x, y, t, ymax

def main():
     import matplotlib.pyplot as plt
     air0 = 1.2
     DragB2OverM = 4E-5

     phi=np.pi*35/180
    
     u0=1000
     vel, pos = [], []
     vel += [u0*np.cos(phi)]
     vel += [u0*np.sin(phi)]
     pos += [0]
     pos += [0]
     tstep = 0.1
     t0 = 0
     #
     # First varying the airdensity and g with height
     #================================================
     doVaryG = True
     doVaryDens = True
     xval1, yval1, time1, hmax1 = propagate(pos,vel,t0,tstep,doVaryG,doVaryDens,air0,DragB2OverM)

     #
     # First varying the airdensity and g with height
     #================================================
     doVaryG = False
     doVaryDens = False
     xval2, yval2, time2, hmax2 = propagate(pos,vel,t0,tstep,doVaryG,doVaryDens,air0,DragB2OverM)

     #
     # Make the graphs
     #=================
     print(50*"=")
     print("When varying both air density and g with height")
     print("The H_max = %7.3f \nThe X_max = %7.3f"%(hmax1,xval1[-1]))
     print(50*"=")
     print("When both air density and g are constant")
     print("The H_max = %7.3f \nThe X_max = %7.3f"%(hmax2,xval2[-1]))
     print(50*"=")

     plt.figure(figsize=(12,4))
     plt.subplot(1,3,1)
     plt.plot(time1,xval1,'b-')
     plt.plot(time2,xval2,'r--')
     plt.xlabel('time')
     plt.ylabel('x position')
     plt.text(10,33000,'Varying Air density and g')
     plt.text(10,30000,'Air density and g constant')
     plt.hlines(33500,1,8,linestyle='solid',color='b')
     plt.hlines(30500,1,8,linestyle='dashed',color='r')
     plt.grid(True)
     #
     plt.subplot(1,3,2)
     plt.plot(time1,yval1,'b-')
     plt.plot(time2,yval2,'r--')
     plt.xlabel('time')
     plt.ylabel('y position')
     plt.text(20,1500,'Varying Air density and g')
     plt.text(20,1000,'Air density and g constant')
     plt.hlines(1600,12,18,linestyle='solid',color='b')
     plt.hlines(1100,12,18,linestyle='dashed',color='r')
     plt.grid(True)
     #
     plt.subplot(1,3,3)
     plt.plot(xval1,yval1, 'b-')
     plt.plot(xval2,yval2, 'r--')
     plt.xlabel('x position')
     plt.ylabel('y position')
     plt.text(8500,2100,'Varying Air density and g')
     plt.text(8500,1500,'Air density and g constant')
     plt.hlines(2200,5000,8000,linestyle='solid',color='b')
     plt.hlines(1600,5000,8000,linestyle='dashed',color='r')  
     plt.grid(True)
     #
     plt.tight_layout()
     plt.show()

import numpy as np
main()
