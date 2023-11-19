#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def interpolate(t0,t,x0,x,xpref):
    slope = (x-x0)/(t-t0)
    if slope == 0:
        value = t
    else:
        value = t0 + (xpref - x0)/slope
    return value

def initialise():
    r1 = float(input("The radius of the 1st ball "))
    r2 = float(input("The radius of the 2nd ball "))
    m1 = float(input("The mass of the 1st ball "))
    m2 = float(input("The mass of the 2nd ball "))
    y10 = float(input("The initial height of the 1st ball "))
    y20 = float(input("The initial height of the 2nd ball "))
    v10 = float(input("The initial velocity of the 1st ball "))
    v20 = float(input("The initial velocity of the 2nd ball "))
    Tmax = float(input("The max time interval "))
    tstep = float(input("The time step "))
    t0 = 0
    print()
    print(40*'=')
    print(' Initial conditions for the motion of the balls')
    print(7*' ','Ball 1',3*' ','Ball 2')
    print(' aktina: %4.1f %10.1f'%(r1,r2))
    print(' masses: %4.1f %10.1f'%(m1,m2))
    print(' speeds: %4.1f %10.1f'%(v10,v20))
    print(' height: %4.1f %10.1f'%(y10,y20))
    print(' TimeMx: [0,%4.0f] sec'% Tmax)
    print(' TimeStep:%5.3f sec'%tstep)
    print(40*'=')
    return r1, r2, m1, m2, y10, y20, v10, v20, Tmax, tstep, t0

def Euler_Cromer(m1,m2,r1,r2,t0,y1_0,y2_0,v1_0,v2_0,tmax,dt):
    A1 = (m1-m2)/(m1+m2)
    A2 = 2.0*m2/(m1+m2)
    A3 = 2.0*m1/(m1+m2)
    ypos1, ypos2 = [], []
    velo1, velo2 = [], []
    time = []
    t = t0
    a = -9.81
    v1 = v1_0
    v2 = v2_0
    y1 = y1_0
    y2 = y2_0
    k  = 0
    while t <= tmax+dt :
        if debug and t>0.642 and t<0.877:
            print('%4.3f  %7.5f  %7.5f  %8.5f  %8.5F'%(t,y1,y2,v1,v2))
        ypos1 += [y1]
        ypos2 += [y2]
        velo1 += [v1]
        velo2 += [v2]
        time  += [t]
        y1_prev = y1
        y2_prev = y2
        v1_prev = v1
        v2_prev = v2
        t_prev  = t
        #.... Methodos Euler-Cromer me statheri epitaxynsi
        v1_new = v1_prev + a*dt
        v2_new = v2_prev + a*dt
        y1_new = y1_prev + v1_new*dt
        y2_new = y2_prev + v2_new*dt
        t_new  = t + dt
        #.... Elegxos krousis tis xamiloteris mpalas me to edafos
        if y1_new <= r1 :
            y_kr = r1
            t_kr = interpolate(t_prev, t_new, y1_prev, y1_new, y_kr)
            y1_new = y_kr            # To Kentro Mazas tis mpalas prin kai meta
            y1_prev = y_kr           # tin krousi apexei r1 apo to edafos.
            
            dtnew = t_kr - t_prev    # Tropopoiisi tou xronikou vimatos wste to
            v1_kr = v1_prev + a*dtnew # y1_new na antistoixei sti thesi tou KM 
            v1_new = -v1_kr          # ti stigmi tis krousis. Allagi taxytitas. 
            v1_prev = v1_kr
            v2_new = v2_prev + a*dtnew
            y2_new = y2_prev + v2_new*dtnew
            t_new  = t + dtnew
        #.... Elegxos krousis metaksu twn duo swmatwn
        if (y2_new - y1_new) <= (r1 + r2) : # Apostasi mikroteri twn aktinwn
            
            distance = y2_new - y1_new
            fraction = ((r1+r2) - distance)/distance
            y1 = y1_new - (1.0-m1/(m1+m2))*fraction*distance
            y2 = y1 + (r1+r2)
            if y1 <= r1:
                y1 = r1
                y2 = y1+r1+r2
            t_kr  = interpolate(t_prev, t_new, y1_prev, y1_new, y1)
            dtnew = t_kr - t_prev
            dtn1 = dtnew
            v1_kr = v1_prev + a*dtnew
            t_kr  = interpolate(t_prev, t_new, y2_prev, y2_new, y2)
            dtnew = t_kr - t_prev
            dtn2  = dtnew
            v2_kr = v2_prev + a*dtnew
            v1 = A1 * v1_kr + A2 * v2_kr
            v2 = A3 * v1_kr - A1 * v2_kr
            v1_new = v1
            v2_new = v2
            y1_new = y1
            y2_new = y2
            print("Collision of the two balls")
            print(" t_prev:",t_prev, " t_new:",t_new, "\n"\
                  " y1_prev:",y1_prev, " y1_new:",y1_new, "\n"\
                  " y2_prev:",y2_prev, " y2_new:",y2_new, "\n"\
                  " v1_prev:",v1_prev, " v1_new:",v1_new, "\n"\
                  " v2_prev:",v2_prev, " v2_new:",v2_new)
        y1 = y1_new
        y2 = y2_new
        v1 = v1_new
        v2 = v2_new
        t  = t_new
    return ypos1, velo1, ypos2, velo2, time

#... Graphing
def make_plot(Time,Y1pos, Y2pos,mass1,mass2):    
    plt.figure(figsize=(8,4))
    plt.subplot(1,3,1)
    plt.plot(Time,Y1pos,'b-')
    plt.plot(Time,Y2pos,'r-.')
    plt.xlim(0,40)
    plt.xlabel("Time, t(sec)")
    plt.ylabel("Height, h(m)")
    xline1 = 20
    xline2 = 25
    yline1 = 4.5
    yline2 = 4.1
    plt.hlines(yline1,xline1,xline2,color='b',linestyle='solid')
    plt.hlines(yline2,xline1,xline2,color='r',linestyle='dashed')
    plt.text(xline2+1.0,yline1-0.05,'ball 2')
    plt.text(xline2+1.0,yline2-0.05,'ball 1')
    plt.grid(True)
#
    plt.subplot(1,3,2)
    plt.plot(Time,Y1pos,'b-')
    plt.plot(Time,Y2pos,'r-.')
    plt.xlim(40,70)
    plt.xlabel("Time, t(sec)")
    plt.ylabel("Height, h(m)")
    xline1 = 50
    xline2 = 55
    yline1 = 4.5
    yline2 = 4.1
    plt.hlines(yline1,xline1,xline2,color='b',linestyle='solid')
    plt.hlines(yline2,xline1,xline2,color='r',linestyle='dashed')
    plt.text(xline2+1.0,yline1-0.05,'ball 2')
    plt.text(xline2+1.0,yline2-0.05,'ball 1')
    plt.title('Motion when $m_1$/$m_2$ = %2d'%int(mass1/mass2))
    plt.grid(True)
#
    plt.subplot(1,3,3)
    plt.plot(Time,Y1pos,'b-')
    plt.plot(Time,Y2pos,'r-.')
    plt.xlim(70,100)
    plt.xlabel("Time, t(sec)")
    plt.ylabel("Height, h(m)")
    xline1 = 80
    xline2 = 85
    yline1 = 4.5
    yline2 = 4.1
    plt.hlines(yline1,xline1,xline2,color='b',linestyle='solid')
    plt.hlines(yline2,xline1,xline2,color='r',linestyle='dashed')
    plt.text(xline2+1.0,yline1-0.05,'ball 2')
    plt.text(xline2+1.0,yline2-0.05,'ball 1')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#... Driving code
def main():
    r1, r2, m1, m2, y10, y20, v10, v20, Tmax, tstep, t0 = initialise()
    Yball1,Vball1,Yball2,Vball2,Time = Euler_Cromer(m1,m2,r1,r2,t0,y10,y20,v10,v20,Tmax,tstep)
    make_plot(Time, Yball1, Yball2, m1, m2)
    m1 = 2
    m2 = 1
    Yball1,Vball1,Yball2,Vball2,Time = Euler_Cromer(m1,m2,r1,r2,t0,y10,y20,v10,v20,Tmax,tstep)
    make_plot(Time, Yball1, Yball2, m1, m2)

#debug=False
debug=True
main()

