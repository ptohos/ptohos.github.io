#!/usr/bin/python3

import numpy as np
from random import seed, random
'''	
--------------------------------------------------------------
 MC methodos anazitisis elaxistou mias synartisis 

 H methodos epanalambanei synexws ton ypologismo tis F(x),
 se tyxaia epilegmena simeia tis aneksartitis metablitis x
 se ena diastima [A,B]. An ektelesoume ti diadikasia arketes
 fores tote the exei entopistei to elaxisto, fmin, sto xmin.

 To programma xrisimopoiei tin synartisi F(x) = x^2*exp(-x) x sto [0,4]
 kai tin synartisi f(x,y) = y-x-2x^2 -2xy - y^2 gia tin eyresi megisto
 sto diastima [-2,2] kai [1,3] gia x kai y antistoixa
--------------------------------------------------------------
'''
def func1(x):
    return x**2 * np.exp(-x)

def func2(x,y):
    return y - x - 2*x**2 - 2*x*y - y**2

def find_min(myfunc1, xlims, mctries):
    fmin  = 9.0E9
    for itry in range(mctries):
        x = xlims.min() + (xlims.max() - xlims.min())*random()
        y = myfunc1(x)
        if y <= fmin:
            fmin = y
            xmn = x
    return xmn, fmin

def find_max(myfunc2, xlims, ylims, mctries):
    fmax = -9.0E9
    for itry in range(mctries):
        x = xlims.min() + (xlims.max() - xlims.min())*random()
        y = ylims.min() + (ylims.max() - ylims.min())*random()
        z = myfunc2(x,y)
        if z >= fmax: 
            fmax = z
            xmx = x
            ymx = y
    return xmx, ymx, fmax

#... Main
seed(123456)
#... Elaxisto
xvals=np.array([0.0, 4.0])
fmin = 9.0E9	# Mia polu megali arxika timi gia to minimum
#... Megisto
fmax = -9.0E9   # Mia poly mikri arxika timi gia to megisto
xlims=np.array([-2.0,2.0])
ylims=np.array([ 1.0,3.0])

icases = 6
print('\n %10s  %20s  %30s' % ('MC tries','Minimum of func1','Maximum of func2'))
print('%20s  %11s  %12s  %10s  %14s' % ('xmin', 'f(xmin)', 'xmax', 'ymax', 'f(xmax,ymax)')) 
for itries in range(icases):
    ntries = 10**itries
    xmin, min_func1 = find_min(func1,xvals,ntries)
    xmax, ymax, max_func2 = find_max(func2,xlims,ylims,ntries)
    print('{0:7d} {1:14.6f} {2:10.8f} {3:15.8f} {4:11.8f} {5:11.8f}'.
          format(ntries,xmin,min_func1,xmax,ymax,max_func2))
    
