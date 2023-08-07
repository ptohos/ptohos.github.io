#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#read data
time, displ, error = np.loadtxt('LogLogData.dat',unpack=True)

#theoretical curve
accel = 10.
t  = np.linspace(0.05, 90.5, 181)
x  = 0.5*accel*t*t      

# create the plot
plt.figure(1, figsize=(9.5,4))  # to megethos toy canva toy sxediou

plt.subplot(1,2,1)       # opws eidame ayto mporei na grafei kai ws subplot(121)
                         # Simainei ta plots tha ginoun se 1 grammi kai 2 stiles
                         # kai to sygkekrimeno grafima tha mpei stin aristeri
                         # pleyra toy canva
# Grammiki klimaka                        
plt.plot(t, x, color='C0', label = "theory")
plt.plot(time, displ, 'oC1', label = "data")
plt.xlabel('time (sec)')
plt.ylabel('displacement (m)')
plt.legend(loc='upper left')
plt.grid(True)
#
# Logaritmiki klimaka
plt.subplot(1,2,2)      # Topothetisi tou grafimatos sti deksia thesi
plt.loglog(t, x, color='C0', label='theory')
plt.loglog(time, displ, 'oC1', label='data')
plt.xlabel('time (sec)')
plt.ylabel('displacement (m)')
plt.legend(loc='upper left')
plt.grid(True)
#
plt.tight_layout()
#
plt.savefig('LogLogPlot.pdf')
#
plt.show()
