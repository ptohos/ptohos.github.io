#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Example usage of matplotlib pyplot library

Links:
https://matplotlib.org/stable/api/pyplot_summary.html
'''
import numpy as np
import matplotlib.pyplot as plt
import math
#from myFunctions import *

def myFunc(x):
    return np.cos(x)/x + math.exp(x)

# Get a range of values over pi
x = np.arange(np.pi/100, np.pi, np.pi/100)
y = list(map(myFunc, x))
         
# Create the canvas
plt.figure()

# Draw the plot on the canvas
plt.plot(x, y, "r--")
plt.plot(x, x, "b--")
plt.plot(x, [-a for a in y], "g--")
plt.plot(x, [-a for a in x], "y--")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.text(+0.2, 31.15, r'$+\frac{\cos(x)}{x} + e^{x}$', fontsize=12, color="red")
plt.text(+0.2, 25.15, r'$-\frac{\cos(x)}{x} - e^{x}$', fontsize=12, color="green")
if 0:
    plt.show()
else:
    plt.savefig("example01.png")
    plt.savefig("example01.pdf")

quit()
