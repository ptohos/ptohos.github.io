#!/usr/bin/python3
'''
!--------------------------------------------------------
! Paradeigma oloklirwsis tis methodou mesis timis
! xrisimopoiontas tyxaioys arithmoys
! Efarmogi sti synartisi F(x) = x**2*exp(-x).
! Apotelesma einai -(x^2+2x+2)exp(-x)~1.99446
!--------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

def integrand(x):
    y = x * x * np.exp(-x)
    return y

def monte_carlo_integration(ntr,LowLim,UpLim):
    value=0.
    for i in range(ntr):
        rnd = LowLim + (UpLim-LowLim)* random()
        rvs = integrand(rnd)
        value = value + rvs
    expected_value = (UpLim-LowLim)*(value/ntr)
    return expected_value


ntries = int(input("How many tries to evaluate the integral ? "))
lowlimit = float(input("The low limit of integration "))
hilimit = float(input("The upper limit of integration "))
iseed = 123456
seed(iseed)

result = monte_carlo_integration(ntries,lowlimit, hilimit)
print("After %6d tries, the integral is %10.5f"%(ntries,result))

