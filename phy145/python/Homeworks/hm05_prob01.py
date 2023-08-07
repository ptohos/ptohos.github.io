#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 5*x + 3

def plotfunc():
    x=np.arange(0,2.501,0.01)
    plt.figure(figsize=(8,5))
    plt.plot(x,f(x),'b-')
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


plotfunc()

eps=float(input("Eisagete tin epithumiti akriveia sti lusi [eps=1E-4] "))

intervals = [[0.5,1.0],[1.5,2.0]]       # Duo luseis - ara 2 diastimata
sols = []                               # list gia apothikeusi twn lusewm

for xval_L, xval_R in intervals:
    sol, niters = bisection(f,xval_L, xval_R, eps)
    sols.append(sol)
    print("Solution%d is at x = %6.4f"%(len(sols),sol))
