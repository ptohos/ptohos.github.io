#!/usr/bin/python3

'''====================================================
... H analytiki lysi toy provlimatos aytou ypothetontas
... oti x0 = x(t=0) = 0 kai oti i arxiki taxutita den 
... einai 0 einai:
... u(t) = 8*[1-exp(-0.5t)] + u0*exp(0.5t)
... x(t) = 8*[t-2+2*exp(-0.5t)] + 2u0*[1-exp(-0.5t)]
... Gia to provlima mporeite na ypothesete
... oti i arxiki taxytita einai 0. 
...
... Apo tin eksiswsi tis epitaxunsis, an thesoume a=du/dt=0 
... pou simainei oti to swma exei apoktisei oriaki taxutita
... tha kineitai me taxutita uT, isi me: 
... 4-0.5*uT = 0 => uT = 8m/s
... To swma tha vrethei sto 99% tis oriakis 
... taxytitas ti xroniki stigmi t=9.211s
... otan xrisimopoiisoume xroniko vima 0.001s 
    ==================================================='''   
import numpy as np
import matplotlib.pyplot as plt

def d2xdt2(t,x,u):
    ''' H epitaxunsi '''
    return 4.0 - 0.5*u

def dxdt(t,x,u):
    ''' H taxitita '''
    return u

def main():
    
    a0 = float(input("Give the initial acceleration [a0=4.0m/s2] "))
    u0 = float(input("Give the initial velocity [u0=0m/s] "))
    dt = float(input("Give the time step [dt=0.01] "))
    t0 = 0.0
    x0 = 0.0
    uT = 8.0    # Oriaki taxutita

    VelRK2, XRK2, Time = [],[],[]
    VelTH, XTH = [],[]
    u = u0
    t = t0
    x = x0
    while u <= 0.99*uT :
        k1u = dt*d2xdt2(t,x,u)
        k1x = dt*dxdt(t,x,u)
        k2u = dt*d2xdt2(t+dt,x+k1x,u+k1u)
        k2x = dt*dxdt(t+dt,x+k1x,u+k1u)
        u += 0.5*(k1u+k2u)
        x += 0.5*(k1x+k2x)
        t += dt
        uth = uT*(1-np.exp(-0.5*t)) + u0*np.exp(0.5*t)
        xth = uT*(t-2+2*np.exp(-0.5*t)) + 2*u0*(1-np.exp(-0.5*t))
        VelRK2.append(u)
        XRK2.append(x)
        Time.append(t)
        VelTH.append(uth)
        XTH.append(xth)

    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(Time,XRK2,'bo',label='RK2')
    plt.plot(Time,XTH,'r-',label='Analytic')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)') 
    #
    plt.subplot(1,2,2)
    plt.plot(Time,VelRK2,'bo',label='RK2')
    plt.plot(Time,VelTH,'r-',label='Analytic')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)') 
    plt.axhline(0,8,linestyle=":",color='g')
    #
    plt.tight_layout()
    plt.show()
    #
    VelRK2 = np.array(VelRK2)
    XRK2 = np.array(XRK2)
    VelTH = np.array(VelTH)
    XTH = np.array(XTH)
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(Time,100*abs(XRK2-XTH)/XTH,'bo')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel(r'$\frac{ |\Delta(X_{RK2}-X_{Theory})| }{X_{Theory}} (\%)$ ')
    #
    plt.subplot(1,2,2)
    plt.plot(Time,100*abs(VelRK2-VelTH)/VelTH,'bo')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel(r'$\frac{ |\Delta(V_{RK2}-V_{Theory})| }{V_{Theory}} (\%)$ ') 
    #
    plt.tight_layout()
    plt.show()

main()

