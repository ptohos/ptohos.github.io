#! /usr/bin/python3

import numpy as np

def midpoint(f, a, b, n):
    dx = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + dx/2.0) + i*dx)
    result *= dx
    return result

def func(t):
    return 3*(t**2)*np.exp(t**3)

n = int(input('n: '))
uplim = 1
lolim = 0
numerical = midpoint(func, lolim, uplim, n)
Vup = np.exp(uplim**3)
Vlo = np.exp(lolim**3)
exact = Vup - Vlo
error = exact - numerical
print('n=%d: %.8f, error: %10g' % (n, numerical, error))

