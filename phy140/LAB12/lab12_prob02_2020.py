#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def func1(x):
    return 4*np.exp(-2*x)

def func2(x):
    return 0.5*x**2

def func(x):
    return func1(x) - func2(x)

def d1x(x):
    return -8*np.exp(-2*x) - x
'''================================'''
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
'''============================'''
def bisection(f,a,b,eps):
    fa = f(a)
    fb = f(b)
#
    if fa*fb > 0:
        print('The interval does not contain the solution',fa,fb)
        exit()
#
    iter = 1
    while (b-a) > eps:
        sol = (a+b)/2.0
        fsol = func(sol)
        if fsol == 0:
            print('x=',sol)
            exit()
        if fsol * fa > 0:     # They are on the same side of the function
            a = sol         # Chage of the lower limit
            fa = fsol
        else:
            b = sol         # They are on different sides of the functions
            fc = fsol       # Change the upper limit
        iter = iter + 1
    return sol,iter

#.... Main program

xguess = float(input('Give a first estimate for the solution to start Newton '))
xlo    = float(input('Give the low limit of the interval for the bisection '))
xup    = float(input('Give the upper value of the interval for the bisection '))
epsi   = float(input('Give the desired precision for the solution '))
mxit   = 20
#... Newton
xnewton, flag, niter = newton(xguess,func,d1x,epsi,mxit) 
print('\n ****** Results by Newton''s method *******') 
if flag == 0:
    print('The solution is {:.15e}'.format(xnewton))
    print('{:2d} iteration were needed'.format(niter))
    print('The value of the function is f(x=',xnewton,') = ',func(xnewton))
elif flag == 1:
    print('No solution was reached because no convergence')
    print('{:2d} iteration were used of max {:2d}'.format(niter,mxit))
else:
    print('Derivative is zero at the value {:.2e}'.format(xnewtom))
    print('The value of the function is f(x',newton,') = ',func(xnewton))

#
print('\n ****** Results by Bisection''s method *******') 
xbisect, biter = bisection(func,xlo,xup,epsi)
print('Bisection solution = {:.15e}'.format(xbisect))
print('{:2d} iterations needed\n'.format(biter))

sol = xbisect   # To apotelesma twn 2 methodwn prepei na einai idio
                # gia tin idia akriveia. Apla epilegw ti bisection lysi
                # gia tis anagkes tou plot

'''
 Kanoume to grafima twn duo sunartisewn gia na 
 broume peripou to simeio tomis tous
'''
x = np.arange(0.,2.1,0.1)
#
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,func1(x),'r-')
plt.plot(x,func2(x),'b--')
plt.plot(sol,func1(sol),'o',markersize=15,fillstyle='none')
plt.text(0.4,2.0,r'f(x) = $4e^{-2x}$')
plt.text(1.5,1.0,r'f(x) = $0.5x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
#
plt.subplot(1,2,2)
plt.plot(x,func1(x)-func2(x),'b-')
plt.plot(sol,func(sol),'o',markersize=15,fillstyle='none')
plt.text(0.5,1.5,r'f(x) = $4e^{-2x} - 0.5x{^2}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
plt.axhline(y=0,color='red',linestyle='--')
#
plt.tight_layout()
#
plt.show()
