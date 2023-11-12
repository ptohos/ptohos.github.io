#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3.1416,3.1416,201)
y = np.cos(x)
x2 = x**2
lines=['g-','k-','b-','c-','r-.','r:']

plt.figure(figsize=(6,6))
plt.plot(x,y,'r-')

term = 1
taylor = 1
for j in range(6):
    term *= -x2/(2*j+1)/(2*j+2)
    taylor += term 
    plt.plot(x,taylor,lines[j])
plt.xlim(-np.pi,np.pi)
plt.ylim(-1.01,1.01)
plt.xlabel('Angle x (rad)')
plt.ylabel('cos(x)')
plt.text(-1.6,-0.5,r'$1-\frac{x^2}{2!}$')
plt.text(-3,0.,r'$1-\frac{{x^2}}{{2!}}+\frac{{x^4}}{{4!}}$')
plt.text(-2.5,-0.9,r'$1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}$')
plt.show()
