#!/usr/bin/python3
'''
   Mporoume na grapsoume to oloklirwma sa ti lusi mias
   kanonikis diaforikis eksiswsis dy/dx = cos(x) me 
   arxiki synthiki y(x=-pi/2)=-1 kai i timi y(x=pi/2) tha dwsei
   tin timi tou oloklirwmatos. 
   Tha xrisimopoiisoume ti methodo Euler gia tin oloklirwsi
   tis diaforikis eksiswsis. H analytiki timi einai 2
'''

import numpy as np
from random import seed, random

def Euler(deriv,y0,dx,lowX,uppX):
    yv = []
    xv = []
    yeul = y0
    xeul = lowX
    while xeul <= uppX:
        yv += [yeul]                   # Arxiki sunthiki
        xv += [xeul]
        yeul = yeul + dx * deriv(xeul)
        xeul = xeul + dx
    return xv, yv

def deriv(xx):
    return np.cos(xx)

def func(xx):
    return np.sin(xx)

def MCIntegrate_average(deriv, nMC, lowX, uppX):
    sumit = 0.0
    for i in range(nMC):
        xrand = lowX + (uppX-lowX)*random()
        sumit = sumit + deriv(xrand)
    integral = (uppX-lowX)*sumit/nMC
    return integral

def main():
    dx_step = float(input("Step size [dx = 0.1] "))
    seed(12345)
    lowlimX = -np.pi/2
    upplimX = +np.pi/2
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
 
    ntries = 1000000
    MCInt_result = MCIntegrate_average(deriv, ntries, lowlimX, upplimX)
    print("To oloklirwma tis synartisis cos(x) sta oria oloklirwsis")
    print("[%3.1f,%3.1f] me ti method MC mesis timis einai %14.10f"%
          (lowlimX, upplimX, MCInt_result))
    print("H analytiki lysi einai :%14.10f"% (analytic))
    print(50*('='))
    
main()
