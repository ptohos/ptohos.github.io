#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
x0=-np.pi/2
y0=0
xp=10
n=101
step_h=(xp-x0)/(n-1)
x=np.linspace(x0,xp,n)
y=np.zeros([n])
y[0]=y0
for k in range(1,n):
y[k]=y[k-1]+step_h*(y[k-1]/x[k-1])+(x[k-1])*(np.sin(x[k-1])))
for k in range(n):
    print(x[k],y[k])
t=np.linspace(-(np.pi/2),10.,400)
a = -t*(np.cos(t))
plt.plot(t, a, 'r-')
plt.plot(x,y,'o')
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.title(u"Approximate Solution with Euler’s Method")
plt.show()
