#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def Trapezoidal(f, a, b, n):
    dx = (b-a)/float(n)      # Eyros ypodiastimatos - n arithmos ypodiastimatwn
                            # a kai b katw kai panw orio oloklirwsis
    s = 0.5*(f(a) + f(b))   # H prwti kai teleutaia pleyra 
    for i in range(1,n):
        s = s + f(a + i*dx)  # H timi tis synartisis sta endiamesa diastimata 
    return dx*s

def g(t):
    return np.exp(-t**4)

a = -2;  b = 2             # panw kai katw orio
n = 1000                   # arithmos upodiastimatwn
result = Trapezoidal(g, a, b, n)
print("For Nsteps  = %5d the integral of the function exp(-x**4) in the range [-2,2] is %7.5f"%(n,result))

