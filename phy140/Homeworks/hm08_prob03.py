#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random

def func(x):
    a = np.sum(x)
    return a*a

def integrate_mc(Func, xlims, mctries):
    sum   = 0.0
    sumsq = 0.0
    first = True
    norm  = 1
    xv = np.array([0.,0.,0.,0.,0.,0.])
    for itries in range(mctries):
        if itries>0: first = False
        for i in range(6):
            xr = xlims[i,0] + (xlims[i,1] - xlims[i,0])*random()
            xv[i]  = xr
            if first:
                norm = norm*(xlims[i,1]-xlims[i,0])

        sum = sum + Func(xv)
        sumsq = sumsq + Func(xv) * Func(xv)
    integral = norm * sum/mctries
    sum = sum/mctries
    sumsq = sumsq/mctries
    error = norm*np.sqrt((sumsq - sum*sum)/mctries)
    return integral,error

#... Main

seed(123456)
xvalues=np.array([[0.,1.],[0.,1.],[0.,1.],
                  [0.,1.],[0.,1.],[0.,1.]])
print(xvalues)
ntot = 21
base = 2

my_file = open('Askisi3.dat','w')
for i in range(ntot):
    mc_integral,mc_error = integrate_mc(func,xvalues,base)
    base *= 2
    if i == 0:
        my_file.write('%9s %12s %10s\n'%('MCtries','Integral','Error'))
    my_file.write('%8d %12.5f %12.5f\n'%(base,mc_integral,mc_error))

