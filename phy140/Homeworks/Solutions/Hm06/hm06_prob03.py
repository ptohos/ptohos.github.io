#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
#
def deriv(tempe):
    const1 = -2.2067E-12
    const2 = 81E8
    result = (((const1*tempe)*tempe)*tempe)*tempe - const1*const2
    return result

'''
  Parts (a) and (b)
'''
time_step = 30
time  = 0
target_time =  480
init_temp   = 1200
final_temp  =  320
temp = init_temp
keep_doing  = True
while keep_doing:
    temp_prev = temp            # The time and temperature
    time_prev = time            # at the beginning of the interval
    temp_eu = temp + time_step * deriv(temp)   # Euler step to find the temp
                                               # sto telos tou diastimatos
    temp_ec = temp + time_step * deriv(temp_eu)# Euler-Cromer step: Use the
                                               # deriv sto telos tou diastimato
                                               # gia na kanoume to Euler step
    time += time_step
    temp  = temp_ec
    if time == target_time:       # Part(a)
        print("The temperature at time %4.0f is %8.4f"%(time,temp_ec))

    if temp_ec < final_temp:      # Part(b)
        keep_doing = False
        ''' Use linear interpolation to find the exact time'''
        slope = (temp_ec - temp_prev)/(time-time_prev)
        time_req = (final_temp - temp_prev)/slope + time_prev
        print("The moment the sphere has temperature equal to %4.0f is %6.3f"%
              (final_temp, time_req))

dt = 15
nsteps = 6
tsteps = []
temps  = []
for istep in range(nsteps):
    target_time =  480
    init_temp   = 1200
    temp  = init_temp
    time  = 0
    keep_doing  = True
    while keep_doing:
        temp_eu = temp + dt * deriv(temp)
        temp_ec = temp + dt * deriv(temp_eu)

        time += dt
        temp  = temp_ec
        if time == target_time:
            temps  +=[temp]
            tsteps +=[dt]
            keep_doing = False
    dt *=2               # double the time step
    
plt.figure(figsize=(6,6))
plt.plot(tsteps,temps,'bo')
plt.xlabel('Time step, dt (s)')
plt.ylabel(r'Temperature, $\theta$ ($^o$K)')
plt.xlim(0,500)
plt.show()

