#!/usr/bin/python3
'''
Methodos Newton-Raphson gia euresi rizas
Gia tin thetiki lusi tis sunartisis 
i arxiki timi pou xrisimopoieitai einai x0=2
Enw gia timi tou x0=1 i methodos epistrefei
tin arnitiki lusi.
H parakatw efarmogi einai ligo diaforopoiimeni
apo tis dialeksis pou deixnei tin idea
tis methodou
'''
import numpy as np
#
def func(x):
    return 5.0 + 4.0*x - np.exp(x)
#
def deriv(x):
    return 4.0 - np.exp(x)
#
def newton(x0,f,df,eps,istepmx):
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error    # The new solution 
        x0 = x1            # The new solution becomes the old solution for the
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1
            break
#
    return x0,flag,istep

# Main 
xinit = float(input("Give the low limit "))
eps = float(input("Give the desired accuracy "))
itermx = int(input("Give the max numbers of iterations for convergence "))
#
sol,flag,iter = newton(xinit,func,deriv,eps,itermx)
#
if flag == 0:
    print('The solution is {:.2e}'.format(sol))
    print('{:2d} iteration were needed'.format(iter))
    print('The value of the function is f(x=',sol,') = ',func(sol))
elif flag == 1:
    print('No solution was reached because no convergence')
    print('{:2d} iteration were used of max {:2d}'.format(iter,iterx))
else:
    print('Derivative is zero at the value {:.2e}'.format(sol))
    print('The value of the function is f(x',sol,') = ',func(sol))


