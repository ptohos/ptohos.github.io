#!/usr/bin/python3
'''
  To programma efarmozei ti methodo brute-force gia tin 
  euresi tou megistou tis sunartisis pros oloklirwsi. 
  To akrotato brisketai zitontas i paragwgos na midenizetai 
'''

import numpy as np
from random import seed, random

def func1(x):
    return -x**np.pi + np.pi*x

#... H 1-i paragwgos tis sunartisis func1
def d1x(x):
    return -np.pi*x**(np.pi-1) + np.pi


'''====================
   Kurio programma
   ====================='''
lower_x  = float(input("Give the lower value of x: "))
upper_x  = float(input("Give the upper value of x: "))
dx       = float(input("Give the step size of changing x: "))

nsteps = int((upper_x - lower_x)/dx)
x = [lower_x + i*dx for i in range(nsteps+1)]
y = list(map(d1x,x))

root = None

for i in range(len(x)-1):
    if y[i]*y[i+1] < 0:
        root = x[i] -  (x[i+1] - x[i])/(y[i+1] - y[i]) * y[i] 
        break
    elif y[i] == 0 :
        root = x[i]
        break

if root is None:
    print('Could not find any root in [%g, %g]' % (x[0], x[-1]))
else:
    print('The derivative is zero for x=%g' % root)
    print('The corresponding value of y (ymax) is %5.4f' % func1(root))

