#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Read data from a file 
xdata, ydata, yerror = np.loadtxt("DataWithErrors.dat",unpack=True)

# Create theoretical curve
x = np.linspace(0,45,128)
y = 1.1 + 3.0 * x * np.exp(-(x/10.0)**2)

# creat plot
plt.figure(1,figsize=(8,6))
plt.plot(x,y,'-C0', label="theory")
plt.errorbar(xdata,ydata, fmt='oC1', label='data',
             xerr=0.75, yerr=yerror, ecolor='black')
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right')
plt.savefig('DataWithErrors.pdf')
plt.show()
