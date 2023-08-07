#!/usr/bin/python3
'''
For N nuclei of a radioactive substance at time t, the decay rate 
dN/dt is given by:

 tau dN/dt = -N
=> dN/dt = -N/tau
=> N (t) = No exp(-t/tau) 
where No = N(t=0).

At the time of the decay constant, i.e. t = tau, 
the number of radioactive nuclei is about a third of the initial population:
N(t=tau) = No/exp(1) = No/0.37
'''
import numpy as np
import matplotlib.pyplot as plt

def Euler(N, t, dt, tau, nSteps):
    NList = []
    tList = []
    
    for i in range(0, nSteps):

        NList.append(N)
        tList.append(t)
        
        # Evaluate the slope (derivative) at the start of the time interval
        # This gives the decay rate!
        dNdt = -N/tau

        # Evaluate the slope (derivative) at the end of the time interval
        N = N + dNdt * dt

        # Increment time interval
        t = t + dt
    return tList, NList
        
# Define variables
t0     = 0.0  # seconds
tMax   = 5.0  # seconds
dt     = 0.05 # seconds
nSteps = int( (tMax - t0)/dt)
N0     = 1000 # initial number of nuclei population
t0     = 0.0
tau    = 1.0 #1.0/1.55E-10 # lambda = 1/tau


xList, yList = Euler(N0, t0, dt, tau, nSteps)
plt.figure()
#plt.plot(xList, yList, 'ko-', lw=2, label= r"Radioactive decay ($\tau = %.1f s$)" % (tau) )
plt.plot(xList, yList, 'ko-', lw=2, label= r"Radioactive decay")
plt.xlabel('t (s)')
plt.ylabel('N (t)')
plt.axvline(x=tau, color='r',linestyle='--', label=r"decay constant $\tau$ = %0.1f s" % (tau) )
plt.axhline(y=N0/np.exp(1.0), color='r',linestyle='--')

plt.axvline(x=0, color='b',linestyle='--', label=r"$N_{t=0} = %0.0f$" % (N0) )
plt.axhline(y=N0, color='b',linestyle='--')
plt.legend() #title="Parameters: ")
plt.show()
