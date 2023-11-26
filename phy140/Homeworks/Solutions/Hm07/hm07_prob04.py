#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random

def func(x):
    return np.sin(x)

def integrate_mc(Func, xlims, mctries):
    sum   = 0.0
    sumsq = 0.0
    for itries in range(mctries):
        x = xlims.min() + (xlims.max() - xlims.min())*random()
        sum = sum + Func(x)
        sumsq = sumsq + Func(x) * Func(x)
    integral = (xlims.max() - xlims.min()) * sum/mctries
    sum = sum/mctries
    sumsq = sumsq/mctries
    error = (xlims.max() - xlims.min())*np.sqrt((sumsq - sum*sum)/mctries)
    return integral,error

#... Main

seed(123456)
xvalues=np.array([0.,np.pi])
ntot = 17
base = 2

my_file = open('Integral.dat','w')
for i in range(ntot):
    mc_integral,mc_error = integrate_mc(func,xvalues,base)
    base *= 2
    if i == 0:
        my_file.write('%8s %11s %10s\n'%('MCtries','Integral','Error'))
    my_file.write('%6d %12.5f %12.5f\n'%(base,mc_integral,mc_error))

