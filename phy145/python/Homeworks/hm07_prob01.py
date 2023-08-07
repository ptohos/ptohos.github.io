#!/usr/bin/python3
'''
   Mporoume na grapsoume to oloklirwma sa ti lusi mias
   kanonikis diaforikis eksiswsis dy/dx = 6x^3 me 
   arxiki synthiki y(x=5)=0 kai i timi y(x=8) tha dwsei
   tin timi tou oloklirwmatos. 
   H methodos RK2 xrisimopoiei ti mesi timi tis paragwgou
   stin arxi kai sto telos tou ekastote upodiastimatos dx
   gia na kanei ena vima euler
'''

import numpy as np

def RK2(myfunc,y0,dx,lowX,uppX):
    N_x = int(round((uppX-lowX)/dx))   # Arithmos ypodiastimatwn
    yv = np.zeros(N_x+1)               # Initialization twn timwn tou y
    xv = np.linspace(lowX, uppX, N_x+1)
    yv[0] = y0                         # Arxiki sunthiki
    for n in range(N_x):
        y_temp = yv[n] + dx * myfunc(yv[n],xv[n])
        rk2_deriv = 0.5 * (myfunc(yv[n],xv[n])+myfunc(yv[n+1],xv[n+1]))
        yv[n+1] = yv[n] + dx * rk2_deriv
    return yv,xv

def simpson(myfunc, dx, lowX, uppX):
    ndiv = int((uppX - lowX)/dx)   # Arithmos upodiastimatwn
    result = -999
    if ndiv % 2 != 0:
        print("Prepei na yparxei artio plithos diastimatwn")
        exit()
    result = 0
    y = 0
    for i in range(0,ndiv-1,2):    # Loop ws pros ton arithmo to plithos
        xa = lowX + i * dx         # twn oriwn (simeiwn) twn ypodiastimatwn
        xb = lowX + (i+1) * dx     # Yparxoun ndiv+1 simeia gia ndiv diastimata
        xc = lowX + (i+2) * dx
        result += myfunc(y,xa) + 4*myfunc(y,xb) + myfunc(y,xc)
    result *= dx/3
    return result

def myfunc(yy,xx):
    return 6*xx**3

def main():
    lowlimX = float(input("Low limit of integration [lowX = 5] "))
    upplimX = float(input("Upper limit of integration [uppX = 8] "))
    dx_step = float(input("Step size [dx = 0.15] "))
    y0 = 0  # Arxiki sunthiki
    F = lambda x: 3/2*x**4
    analytic = F(upplimX) - F(lowlimX)

    yvalues, xvalues = RK2(myfunc,y0,dx_step,lowlimX,upplimX)
    rk2_result = yvalues[-1] - yvalues[0]
    print(50*('='))
    print("To oloklirwma tis synartisis 6x^3 sta oria oloklirwsis")
    print("[%3.1f,%3.1f] me ti method RK2 einai %14.10f"%
           (lowlimX, upplimX, rk2_result))
    print("H analytiki lysi einai :%14.10f"% (analytic))
    print(50*('='))
    simp_result = simpson(myfunc, dx_step, lowlimX, upplimX)
    print("To oloklirwma tis synartisis 6x^3 sta oria oloklirwsis")
    print("[%3.1f,%3.1f] me ti method Simpson einai %14.10f"%
          (lowlimX, upplimX, simp_result))
    print("H analytiki lysi einai :%14.10f"% (analytic))
    print(50*('='))
    
main()
