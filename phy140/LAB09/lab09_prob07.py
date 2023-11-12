#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = Symbol('x')
expr = cos(x)
expand=expr.series(x, 0, 5).removeO()
print(expand)
expansion = lambdify(x,expand)
x=[-np.pi/2+k*0.01 for k in range(315)]
yvals=[np.cos(xvals) for xvals in x]        #  yvals=list(map(np.cos,x))
yvexp=[expansion(xvals) for xvals in x]     #  yvexp=list(map(expansion,x))

plt.figure(figsize=(6,4))
plt.plot(x,yvals,'b-')
plt.plot(x,yvexp,'r--')       
plt.xlabel('x (radians)')
plt.ylabel('cos(x)')
plt.hlines(y=0.95, xmin=-1.7, xmax=-1.5, colors='blue', linestyles='solid')
plt.hlines(y=0.85, xmin=-1.7, xmax=-1.5, colors='red', linestyles='dashed')
plt.text(-1.47,0.93,r'cos(x)')
plt.text(-1.47,0.83,r'$f(x)=1-\frac{x^2}{2}+\frac{x^4}{24}$')
plt.show()



