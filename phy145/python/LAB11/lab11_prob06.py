#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import RandomState


t = RandomState(123456)

x = -0.5
sigmaT = 1                       # uncertainty in Temperature
xv = []
Tuns = []
Tsmr = []
for i in range(10):
    x = x + 1.0                  # position along the rod
    Tuns.append(10.0*x)          # mean temperature at this position
    Tsmr.append(t.normal(Tuns[i],sigmaT)) # Draw a random number from a gaussian
                                 # with mean T kai sigma sT. Tha mporousame
                                 # na kanoume to idio pernontas enan tyxaio
                                 # arithmo apo gaussian me mean 0 kai sigma 1
                                 # kai na grapsoyme Tsmear = T + sT*t.normal()
    
    xv.append(x)

plt.figure(figsize=(6,4))
plt.plot(xv,Tsmr,'bo')
plt.plot(xv,Tuns,'r')
plt.xlabel('x pos (cm)')
plt.ylabel('Temperature (C)')
plt.xlim(0.,10.)
plt.grid(True)
plt.show()
