#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import math as math

xList = [0.01*x for x in range(0, 300, 1)]
yList = [np.exp(x) for x in xList]
y1List= [1 + x for x in xList]
y2List= [1 + x + x**2/2 for x in xList]
y3List= [1 + x + x**2/2 + x**3/math.factorial(3) for x in xList]
y4List= [1 + x + x**2/2 + x**3/math.factorial(3) + x**4/math.factorial(4) for x in xList]
    
plt.figure()
plt.plot(xList, yList, 'k-', lw=2, label= r"$e^{x}$")

plt.plot(xList, y1List, 'r-', lw=2, label= r"Taylor $1^{st}$ order")
plt.plot(xList, y2List, 'b-', lw=2, label= r"Taylor $2^{nd}$ order")
plt.plot(xList, y3List, 'g-', lw=2, label= r"Taylor $3^{rd}$ order")
plt.plot(xList, y4List, 'y-', lw=2, label= r"Taylor $4^{th}$ order")
plt.xlabel('x')
plt.ylabel('f (x)')
plt.legend(title="")
plt.show()
