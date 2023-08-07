#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

xmin = 0.0
xmax = np.pi
step = np.pi/500.

NSteps = int((xmax - xmin)/step)

filename = 'fourier.dat'
outfile = open(filename,'w')
xval, fval = [], []
vsum1, vsum5, vsum10, vsum100 = [], [], [], []
sum1, sum5, sum10, sum100 = 0,0,0,0
str = '%7.4f %4.1f' + 4*' %7.4f' + '\n'
for i in range(NSteps):
    x = (i-1) * step         # eyresi tou x
    if x < 0 :               # H timi tis sunartisis vimatos
        func = -1.0          # An einai mikroteri tou 0 tote f(x)=-1 
    else :                   # diaforetika 
        func = 1.0           # f(x) = +1

    sum = 0.0                # midenismos tis seiras gia kathe neo x
    for j in range(1,101):   # zitountai to polu 100 oroi [f_100]
        term = np.sin(j*x)/j
        term = term * 2.*(1.0-(-1.0)**j)/np.pi
        sum = sum + term
        if j == 1  : sum1   = sum   # ypologismos twn f1,f5,f10,f100
        if j == 5  : sum5   = sum   # mesa sto idio loop afou oi megistoi
        if j == 10 : sum10  = sum   # oroi pou zitame einai 100 simainei
        if j == 100: sum100 = sum   # oti tha ypologisw to sum gia 1,5,10

        outfile.write(str % (x,func,sum1,sum5,sum10,sum100))
        xval    += [x]
        fval    += [func]
        vsum1   += [sum1]
        vsum5   += [sum5]
        vsum10  += [sum10]
        vsum100 += [sum100]
outfile.close()
        
plt.figure(figsize=(6,6))
plt.plot(xval,fval,'k-')
plt.plot(xval,vsum1,'c:')
plt.plot(xval,vsum5,'m-.')
plt.plot(xval,vsum10,'b--')
plt.plot(xval,vsum100,'r-')
plt.xlim(xmin,xmax)
plt.ylim(0,1.4)
plt.xlabel('x (radians)')
plt.ylabel('f(x)')
plt.title('Fourier representation of step function')
plt.text(1.0,0.80,'f(x)')
plt.text(1.0,0.74,r'$S_1$')
plt.text(1.0,0.68,r'$S_5$')
plt.text(1.0,0.62,r'$S_{10}$')
plt.text(1.0,0.56,r'$S_{100}$')
plt.hlines(0.81,0.83,0.98,color='black',linestyle='solid')
plt.hlines(0.75,0.83,0.98,color='cyan',linestyle='dotted')
plt.hlines(0.69,0.83,0.98,color='magenta',linestyle='dashdot')
plt.hlines(0.63,0.83,0.98,color='blue',linestyle='dashed')
plt.hlines(0.57,0.83,0.98,color='red',linestyle='solid')
plt.show()
 
