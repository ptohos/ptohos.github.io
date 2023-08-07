#!/usr/bin/python3

import sys
import numpy as np
import math

def Bisection(f, dfl, lowl, uppl, eps, n):
    x_L = lowl
    x_R = uppl
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("Error! Function does not have opposite \
              signs at interval endpoints!")
        sys.exit(1)
    x_M = (x_L + x_R)/2
    f_M = f(x_M)
    iteration_counter = 1

    while abs(f_M) > eps:
        if f_L*f_M > 0:   # i.e., same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = (x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter += 1
    return x_M, iteration_counter

def Newton(f, df, lowl, uppl, eps, n):
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

def Secant(f, dfl, lowl, uppl, eps, n):
    x0   = lowl
    x1   = uppl
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = (f_x1 - f_x0)/(x1 - x0)
            x = x1 - f_x1/denominator
        except:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)     # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
    if abs(f_x1) > eps:
        iteration_counter = -1
        
    return x, iteration_counter

def BruteForce(f, dfl, lowl, uppl, eps, n):
    x = np.linspace(lowl, uppl, n)
    y = f(x)
    root = None
    for i in range(len(x)-1):
        if y[i] * y[i+1] < 0:
            root = x[i] - (x[i+1]-x[i])/(y[i+1]-y[i])*y[i]
            break
    if root is None:
        print("No root is found in [%g,%g]"%(x[0],x[-1]))
    return root,i+1

def main():
    def f1(x):
        return x**2 - 53
    def df1(x):
        return 2*x

    lowL = float(input("Give the low edge of the interval "))
    uppL = float(input("Give the upper edge of the interval "))
    epsi = float(input("Give the desired accuracy of the solution "))
    meth=['BruteForce','Bisection','Newton','Secant']
    methods=[BruteForce,Bisection,Newton,Secant]
    print(50*'-')
    print("  Method         Solution      No. iterations")
    print(50*'-')
    j=0
    for method in methods:
        solution, iter = method(f1, df1, lowL, uppL, epsi, 1000)
        print(' %10s    %11.8f  \t  %3d'%(meth[j],solution,iter))
        j += 1
    print(50*'-')

main()
