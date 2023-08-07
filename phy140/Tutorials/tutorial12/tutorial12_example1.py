#!/usr/bin/python3

import numpy as np
from math import asin
import matplotlib.pyplot as plt
from random import seed, random

def PDF(x):
    return np.cos(x)

xlo = float(input("Give the lower value of the desired x-interval [-pi/2] "))
xup = float(input("Give the upper value of the desired x-interval [ pi/2] "))
Ntries = int(input("How many random numbers to generate [100K]? "))

seed(123456)

yvl = []
norm = (np.sin(xup) - np.sin(xlo))
for itry in range(Ntries):
    xv = random()           # epilogi tuxaias timis metaksu [0,1)
    xv = norm*xv - 1        # sin(x) = 2y-1
    yvl.append(asin(xv))    # x = arcsin(2y-1)

plt.figure(figsize=(6,6))
cont,xbinval,intr=plt.hist(yvl,bins=100,range=(-np.pi/2,np.pi/2),density=True,
                           histtype='step',color='g')

ypdf=PDF(xbinval)/norm
plt.plot(xbinval,ypdf,'b-',label=r'PDF:cos(x)')
plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number distributed according to $cos(x)$')
plt.axis([-np.pi/2,np.pi/2,0.,0.55])
plt.grid(True)
plt.legend()
plt.show()
