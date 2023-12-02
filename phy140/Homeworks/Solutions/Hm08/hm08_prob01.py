#!/usr/bin/python3
'''
   Mporoume na grapsoume to oloklirwma sa ti lusi mias
   kanonikis diaforikis eksiswsis dy/dx = cos(x) me 
   arxiki synthiki y(x=0)=0 kai i timi y(x=pi) tha dwsei
   tin timi tou oloklirwmatos. 
   Tha xrisimopoiisoume ti methodo Euler gia tin oloklirwsi
   tis diaforikis eksiswsis. H analytiki timi einai 0
   kai dn exei endiaferon. 

   H askisi pou lunw edw einai i dy/dx= sin(x) pou prokupte
   apo ti sunartisi -cos(x) kai arxiki timi gia x=0, -1
   To oloklirwma einai 2. 

   Tha prepei na allaksete tin sunartisi deriv kai func

'''

import numpy as np

def Euler(deriv,y0,dx,lowX,uppX):
    N_x = int(round((uppX-lowX)/dx))   # Arithmos ypodiastimatwn
    yv = np.zeros(N_x+1)               # Initialization twn timwn tou y
    xv = np.linspace(lowX, uppX, N_x+1)
    yv[0] = y0                         # Arxiki sunthiki
    for n in range(N_x):
        yv[n+1] = yv[n] + dx * deriv(xv[n])
    return xv, yv

def Trapezoidal(f, a, b, dx):
    n  = int((b - a)/dx)    # Arithmos upodiastimatwm
    s = 0.5*(f(a) + f(b))   # H prwti kai teleutaia pleyra 
    for i in range(1,n):
        s = s + f(a + i*dx)  # H timi tis synartisis sta endiamesa diastimata 
    return dx*s

def deriv(xx):
    return np.sin(xx)

def func(xx):
    return -np.cos(xx)

def main():
    dx_step = float(input("Step size [dx = 0.1] "))
    lowlimX = 0.0
    upplimX = np.pi
    y0 = func(lowlimX)  # Arxiki sunthiki
    analytic = func(upplimX) - func(lowlimX)

    xvalues, yvalues = Euler(deriv,y0,dx_step,lowlimX,upplimX)
    euler_result = yvalues[-1] - yvalues[0]    
    print(50*('='))
    print("To oloklirwma tis synartisis cos(x) sta oria oloklirwsis")
    print("[%3.1f,%3.1f] me ti method Euler einai %14.10f"%
           (lowlimX, upplimX, euler_result))
    print("H analytiki lysi einai :%14.10f"% (analytic))
    print(50*('='))
    trap_result = Trapezoidal(deriv, lowlimX, upplimX, dx_step)
    print("To oloklirwma tis synartisis cos(x) sta oria oloklirwsis")
    print("[%3.1f,%3.1f] me ti method Trapeziou einai %14.10f"%
          (lowlimX, upplimX, trap_result))
    print("H analytiki lysi einai :%14.10f"% (analytic))
    print(50*('='))
    
main()
