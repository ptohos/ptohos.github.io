#!/usr/bin/python3

import numpy as np

def func1(x):
    return np.exp(-x**4)

def func2(x):
    return 3*(x**2)*np.exp(x**3)

def Midpoint(f, a, b, n):
    dx = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + dx/2.0) + i*dx)
    result *= dx
    return result

def Trapezoidal(f, a, b, n):
    dx = (b-a)/float(n)     # Eyros ypodiastimatos - n arithmos ypodiastimatwn
                            # a kai b katw kai panw orio oloklirwsis
    s = 0.5*(f(a) + f(b))   # H prwti kai teleutaia pleyra 
    for i in range(1,n):
        s = s + f(a + i*dx)  # H timi tis synartisis sta endiamesa diastimata 
    return dx*s

problems = [(func1,-2, 2),  # list of (function, a, b)
            (func2, 0, 1)]

methods = (Midpoint, Trapezoidal)
result = []
for k in range(1,13):
    for func, a, b in problems:
        for method in methods:
            n = 2**k + 1
            I = method(func, a, b, n)
            result.append((I, method.__name__, func.__name__, n))
# write out results, nicely formatted:
for I, method, integrand, n in result:
    print('%12s %4s  N=%5d  I=%g' % (method, integrand, n, I))
