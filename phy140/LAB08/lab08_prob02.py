#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt


def func1(x):
    return 4*np.exp(-2*x)

def func2(x):
    return 0.5*x**2

def func(x):
    return func1(x) - func2(x)


xlo    = float(input('Give the low value of the x range '))
xup    = float(input('Give the upper value of the x range '))
dx     = float(input("Give the step size of changing x: "))

nsteps = int((xup - xlo)/dx)
x = [xlo + i*dx for i in range(nsteps+1)]
y = list(map(func,x))

root = None

for i in range(len(x)-1):
    if y[i]*y[i+1] < 0:
        root = x[i] -  (x[i+1] - x[i])/(y[i+1] - y[i]) * y[i] 
        break
    elif y[i] == 0 :
        root = x[i]
        break

if root is None:
    print('Could not find any root in [%g, %g]' % (x[0], x[-1]))
    quit()
else:
    print('The solution is for x=%5.4f' % root)


sol = root   # To apotelesma twn 2 methodwn prepei na einai idio
             # gia tin idia akriveia. Apla epilegw ti bisection lysi
             # gia tis anagkes tou plot

'''
 Kanoume to grafima twn duo sunartisewn gia na 
 broume peripou to simeio tomis tous
'''
#
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,list(map(func1,x)),'r-')
plt.plot(x,list(map(func2,x)),'b--')
plt.plot(sol,func1(sol),'o',markersize=15,fillstyle='none')
plt.text(0.4,2.0,r'f(x) = $4e^{-2x}$')
plt.text(1.5,1.0,r'f(x) = $0.5x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
#
plt.subplot(1,2,2)
plt.plot(x,y,'b-')
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
