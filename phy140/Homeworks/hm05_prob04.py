#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import sys

def factor(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact

def B(L,r):
    a1 = factor(r)
    a2 = factor(2*L - 2*r)
    a3 = factor(L - r)
    a4 = factor(L - 2*r)
    return (-1)**r * a2/(a1*a3*a4)

def Legendre(x):
    L = 8
    A = 0.5**L
    s = 0
    for r in range(int(0.5*L+1)):
        s += B(L,r) * x**(L-2*r)
    return A*s

def Newton(f,x1,x2,eps):
    f_x1 = f(x1)
    f_x2 = f(x2)
    it_counter = 0
    while np.abs(f_x2) > eps and it_counter < 100:
        try:
            denominator = float((f_x2 - f_x1)/(x2 - x1))
            x = x2 - float(f_x2)/denominator
        except ZeroDivisionError:
            print('Error! - denominator is zero for x = ',x)
            sys.exit(1)
        x1 = x2
        x2 = x
        f_x1 = f_x2
        f_x2 = f(x2)
        it_counter += 1
    if abs(f_x2) > eps:
        it_counter = -1
    return x, it_counter

def main():
    mxroot = 4
    x0 = float(input("Initital value for x = "))
    eps = 1E-6
    dx = 0.05
    filename1 = 'Legendre.dat'
    filename2 = 'LegendreRoots.dat'
    outfile1 = open(filename1,'w')
    outfile2 = open(filename2,'w')

    xv = [x0 + k * dx for k in range(int(2*np.abs(x0)/dx)+1)]
    yv = [Legendre(x) for x in xv]
    outfile1.write('%6.4f   %6.4f\n'%(xv[0],yv[0]))
    nroot = 0
    xroot = []
    for i in range(1,len(xv)) :
        xprev = xv[i-1]
        yprev = yv[i-1]
        xnew = xv[i]
        ynew = yv[i]
        outfile1.write('%6.4f   %6.4f\n'%(xv[i],yv[i]))
        if ynew * yprev < 0 and xnew < 0 : # examine whether there sign change
            root, ic  = Newton(Legendre,xprev,xnew,eps)
            nroot += 1
            if nroot > mxroot :
                print('Too many roots for the polynomial')
                nroot = mxroot
            outfile2.write('%7.6f  %7.6f \n'%(root,np.abs(root)))
            xroot += [ root ]
        
    outfile1.close()
    outfile2.close()

    plt.figure(figsize=(5,5))
    plt.plot(xv,yv)
    plt.xlabel('x values')
    plt.ylabel('Legendre Polynomial P(8,x)')
    plt.xlim(x0,-x0)
    plt.grid(True)
    plt.axhline(y=0,xmin=x0,xmax=-x0,color='blue',linestyle='dashed')
    plt.show()

main()
