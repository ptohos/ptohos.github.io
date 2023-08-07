#!/usr/bin/python3

'''====================================================
   ===================================================='''   
import numpy as np
import matplotlib.pyplot as plt

def dvdt(t,x,u):
    ''' H epitaxunsi '''
    F = -9*np.sinh(x)
    return F/mass

def dxdt(t,x,u):
    ''' H taxitita '''
    return u

def intersection(t0, t, x1_0, x1_1, x2_0, x2_1):
    '''==================================================================
       Gia to xrono sunantisis theloume tin tomi 2 eutheiwn apo to grafima 
       twn x1-t kai x2-t. Oi duo kliseis tha einai:
            a = (x1_1 - x1_0)/(t - t0) kai
            b = (x2_1 - x2_0)/(t - t0).
       Alla t - t0 = dt 
       =================================================================='''
    dt = t - t0
    a = (x1_1 - x1_0)/(dt)
    b = (x2_1 - x2_0)/(dt)
    '''=================================================================
       To simeio tomis ikanopoiei kai tis 2 eksiswseis eutheiwn. 
        x_meet - x1_1
       -------------- = a => x_meet = x1_1 + a*(t_meet-t)    (1)
        t_meet - t
    
        x_meet - x1_1        x_meet - x2_1
       -------------- = a = --------------- = b => a*t_meet - a*t=x_meet - x1_1
         t_meet - t          t_meet - t            b*t_meet - b*t=x_meet - x2_1

       Lunoume to sustima kai exoume: 
       t_meet = [x2_1 - x1_1 + (a-b)*t]/(a-b)
       =================================================================='''
    t_meet = (x2_1 - x1_1 + (a-b)*t)/(a-b)
    x_meet = a * (t_meet - t) + x1_1
    
    return t_meet, x_meet

def main():
    global mass
    dt   = 9.76563E-5
    tmax = 100.0
    v1_0 =   5.0
    v2_0 = -10.0
    x1_0 =  0.0
    x2_0 =  0.0
    t0   =  0.0
    mass =  1.0

    x1   = x1_0
    x2   = x2_0
    v1   = v1_0
    v2   = v2_0
    t    = t0
    
    Xpos1, Xpos2, Time = [],[],[]
    
    while t < tmax:
        Xpos1.append(x1)
        Xpos2.append(x2)
        Time.append(t)
        tpast  = t
        x1past = x1
        x2past = x2
        x1 += dxdt(t,x1,v1)*dt + 0.5 * dvdt(t,x1,v1) * dt**2   # Verlet position
        x2 += dxdt(t,x2,v2)*dt + 0.5 * dvdt(t,x2,v2) * dt**2   # Verlet position
        v1 += dt * (dvdt(t,x1,v1) + dvdt(t,x2,v2))/2.0
        v2 += dt * (dvdt(t,x2,v2) + dvdt(t,x2,v2))/2.0
        t  += dt
        if (x2 > x1):
            break
    t_m, x_m = intersection(tpast,t, x1past, x1, x2past, x2) 

    print(70*('='))
    print('Sunantithikan ti xroniki stigmi t_meet: %5.4f(m) sti thesi: %5.4f(m)'
          %(t_m,x_m))
    print(70*('='))
    
    plt.figure(figsize=(8,5))
    plt.plot(Time,Xpos1,'b-',label='Object1')
    plt.plot(Time,Xpos2,'r-',label='Object2')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)') 
    plt.text(0.4,2.0,r'$V^{1}_{0} = %2.0f m/s$'%(v1_0))
    plt.text(0.2,-1.5,r'$V^{2}_{0} = %2.0f m/s$'%(v2_0))
    plt.show()
    #

main()

