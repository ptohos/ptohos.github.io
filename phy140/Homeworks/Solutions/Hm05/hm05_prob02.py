#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 6*np.cos(x) + x*x - 4

def d1x(x):
    return -6*np.sin(x) + 2*x

def d2x(x):
    return -6*np.cos(x) + 2

def plotfunc():
    x = [-4 + iv*0.01 for iv in range(0,801)]   # Sto diastima [-4 4]
    y = [f(xv) for xv in x]
    plt.figure(figsize=(8,5))
    plt.plot(x,y,'b-')
    plt.axhline(0,linestyle='-.',linewidth=4,color='black')
    plt.grid(True)
    plt.xlim(0,2.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def bisection(f, x_L, x_R, eps, return_x_list=False):
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("Error! Function does not have opposite \
                 signs at interval endpoints!")
        sys.exit(1)
    x_M = (x_L + x_R)/2.0
    f_M = f(x_M)
    iteration_counter = 1
    if return_x_list:
        x_list = []

    while abs(f_M) > eps:
        if f_L*f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = (x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter += 1
        if return_x_list:
            x_list.append(x_M)
    if return_x_list:
        return x_list, iteration_counter
    else:
        return x_M, iteration_counter

def Newton(f, df, lowl, uppl, eps):
    x = lowl
    f_value = f(x)
    iteration_counter = 0

    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/df(x)
        except:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        iteration_counter += 1

    if abs(f_value) > eps:
        iteration_counter = -1  # i.e., lack of convergence
        
    return x, iteration_counter


plotfunc()

eps=float(input("Eisagete tin epithumiti akriveia sti lusi [eps=1E-4] "))

intervals = [[-1.0,1.3],[1.5,3.5]]      # Duo luseis - ara 2 diastimata
sols = []                               # list gia apothikeusi twn lusewm

for xval_L, xval_R in intervals:
    sol, niters = bisection(f,xval_L, xval_R, eps)
    sols.append(sol)
    print("Solution%d is at x = %6.4f"%(len(sols),sol))

mx,nit = Newton(d1x, d2x, -0.5, 0.5, eps)
print("The function has a maximum at x = %6.4f with a value of y=%6.4f"%(mx,f(mx) ))
