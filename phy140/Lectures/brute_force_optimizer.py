#!/usr/bin/python3

from numpy import exp, cos

def f(x):
    return exp(-x**2)*cos(4*x)

def brute_force_optimizer(f, a, b, n):
    x = [a+x*(b-a)/n for x in range(n+1)]
    y = list(map(f,x))
    # maxima kai minima kratoun tous deiktes twn thesewn
    # pou antistoixoun sta (topika) akrotata (maxima i minima)
    minima = []
    maxima = []
    for i in range(1, n-1):
        if y[i-1] < y[i] > y[i+1]:
            maxima.append(i)
        if y[i-1] > y[i] < y[i+1]:
            minima.append(i)

    # What about the end points?
    y_max_inner = max([y[i] for i in maxima])
    y_min_inner = min([y[i] for i in minima])
    if y[0] > y_max_inner:
        maxima.append(0)
    if y[len(x)-1] > y_max_inner:
        maxima.append(len(x)-1)
    if y[0] < y_min_inner:
        minima.append(0)
    if y[len(x)-1] < y_min_inner:
        minima.append(len(x)-1)

    # Return x and y values
    return [(x[i], y[i]) for i in minima], \
           [(x[i], y[i]) for i in maxima]


def demo():
    minima, maxima = brute_force_optimizer(f, 0, 4, 1001)
    print('Minima:', minima)
    print('Maxima:', maxima)

if __name__ == '__main__':
    demo()
    
