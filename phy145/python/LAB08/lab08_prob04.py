#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from math import pow
#========================
# Derivative function
#========================
def deriv(temperature):
    return -2.206E-12 * (pow(temperature,4) - 81E8)

def rk4_fun(f,Time0,Temp0,TempF,dt):
    Temp = []
    Time = []
    time = Time0
    temp = Temp0
    Temp +=[Temp0]
    Time +=[Time0]
    while temp >= TempF :
        k1 = f(temp)
        k2 = f(temp + k1 * dt/2)
        k3 = f(temp + k2 * dt/2)
        k4 = f(temp + k3 * dt)
        temp += (k1 + k2 + k3 + k4)*dt/6 
        time +=dt
        Temp +=[temp]
        Time +=[time]
    return Time,Temp
        
def interpolate(time,temp,target,type):
    value  = -1
    if type == 0:
        dt = time[1]-time[0]
        indx = int((target-time[0])/dt)
        if indx > len(time):
            print("den mporei na brethei i epithumiti termokrasia")
        else:
            value = temp[indx]
    if type == 1:
        slope = (temp[-1]-temp[-2])/(time[-1] - time[-2])
        value = time[-2] + (target-temp[-2])/slope 
    return value

#=======================
# MAIN
#=======================
init_temp = float(input("Input the initial temperature "))
fin_temp  = float(input("Input the final temperature "))
init_time = float(input("Input the initial time "))
fin_time  = float(input("Input the final time "))
dt        = float(input("Input the time step "))

mx_steps  = 6
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
sty=['k-','bp--','ro-.','c^:','m*-','go']
dts = []
temps=[]

for idt in range(mx_steps):
    Time,Temp = rk4_fun(deriv,init_time,init_temp,fin_temp,dt)
    plt.plot(Time,Temp,sty[idt],label=f'step ={dt}')
    flag = 0
    desired_temp = interpolate(Time,Temp,fin_time,flag)
    dts +=[dt]
    temps+=[desired_temp]
    if dt == 30 :
        flag = 1
        desired_time = interpolate(Time,Temp,fin_temp,flag)
        desired_tmp = desired_temp

    del Time
    del Temp
    dt *=2

plt.xlabel('time (s)')
plt.ylabel('Temperature, (K)')
plt.legend()
plt.grid('true')

plt.subplot(1,2,2)
plt.plot(dts,temps,'bo')
plt.xlabel('dt (s)')
plt.ylabel('Temperature (K)')
plt.text(100,775,'Sphere temperature when t=480s')
plt.grid('true')
plt.tight_layout()
plt.show()

print(f"The temperature of the sphere at the time={fin_time} is {desired_tmp:5.2f}")
print(f"The time for the sphere to reach the temperature of {fin_temp}(K) is {desired_time:6.1f}")
