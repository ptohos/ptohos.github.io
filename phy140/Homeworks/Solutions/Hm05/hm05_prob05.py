#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt
#=============================
def Newton(f, dfdx, x, eps):
#=============================
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value)/dfdx(x)
        except:
            print("Error! - derivative zero for x = ", x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        iteration_counter += 1

    # An erthoume edw, eite vrethike mia lusi i exoume fthasei sto max iters
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

#=============================
def f1(x):
#=============================
    return 4*np.exp(-2*x)

#=============================
def f2(x):
#=============================
    return 0.5*x*x

#=============================
def f(x):
#=============================
    return f1(x) - f2(x)

#=============================
def dfdx(x):
#=============================
    return -8*np.exp(-2*x)-x

#=====================================================    
def bisection_Newton(f, dfdx, x_L, x_R, eps, s=0.1):
#=====================================================
    f_L = f(x_L)
    if f_L * f(x_R) > 0:
        print("Error! Function does not have opposite \
                  signs at interval endpoints!")
        sys.exit(1)
    x_M = (x_L + x_R)/2.0
    f_M = f(x_M)
    
    iteration_counter = 1
    interval_Newton = s*(x_R - x_L)    # Orio gia allagi sti methodo Newton

    while (x_R - x_L) > interval_Newton:
        if f_L * f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = float(x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter += 1
        
    solution, no_iterations = Newton(f, dfdx, x_M, eps)
    return solution, (iteration_counter + no_iterations)


eps=float(input("Eisagete tin epithumiti akriveia [eps=1E-5] "))
xlo=float(input("Eisagete to katw orio tou diastimatos [xlo=-3] "))
xup=float(input("Eisagete to panw orio tou diastimatos [xup=+3] "))

solution, no_iterations = bisection_Newton(f, dfdx, xlo, xup, eps)
print("A solution x = %7.5f was reached in %d iterations" % \
                                   (solution,no_iterations))

x=np.arange(-3.,3.1,0.1)
plt.figure(figsize=(8,6))
plt.plot(x,f1(x),'b-',label='f1(x)')
plt.plot(x,f2(x),'r-',label='f2(x)')
plt.plot(x,f(x),'g-.',label='f(x)')
plt.text(-0.05,4.5,r'$f_1(x)=4e^{-2x}$',fontsize=12)
plt.text(2.1,2,r'$f_2(x)=0.5x^2$',fontsize=12)
plt.text(0.3,2.5,r'$f(x)=4e^{-2x} - 0.5x^2$',fontsize=12)
plt.text(solution,0,r'$f(x=%6.5f)=0$'%(solution),fontsize=12)
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([-1,3])
plt.ylim([-1,5])
plt.grid(True)
plt.show()
