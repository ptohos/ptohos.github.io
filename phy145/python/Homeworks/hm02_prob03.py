#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

xmin = 0
xmax = np.pi
step = np.pi/500

filename='fourier.dat'
outfile=open(filename,'w')
mat1 = list()
mat2 = list()
mat3 = list()
mat4 = list()
xval = list()
fun  = list()
for xv in np.arange(xmin,xmax,step):
    if xv < 0:
        func = -1.0
    else:
        func = 1.0
    sumseries = 0.0
    for j in range(100):
        jj = j+1
        term  = np.sin(jj*xv)/jj
        term *= 2*(1.0 - (-1)**jj)/np.pi
        sumseries += term
        if jj == 1:   sum1   = sumseries
        if jj == 5:   sum5   = sumseries
        if jj == 10:  sum10  = sumseries
        if jj == 100: sum100 = sumseries
    outfile.write(' {0:5.3f}  {1:4.2f}  {2:6.5f}  {3:6.5f}  {4:6.5f}  {5:6.5f}'.
                  format(xv,func,sum1,sum5, sum10, sum100))
    mat1 += [sum1]
    mat2 += [sum5]
    mat3 += [sum10]
    mat4 += [sum100]
    xval += [xv]
    fun  += [func]

plt.figure(figsize=(6,6))
plt.plot(xval,mat1,'m--',label='sum1')
plt.plot(xval,mat2,'b:', label='sum5')
plt.plot(xval,mat3,'r-.',label='sum10')
plt.plot(xval,mat4,'g-', label='sum100')
plt.plot(xval,fun,'k-', label='step')
plt.title('Fourier representation of the step function')
plt.legend()
plt.xlabel('x')
plt.ylabel(r'f_N')
plt.xlim(0,np.pi)
plt.show()
