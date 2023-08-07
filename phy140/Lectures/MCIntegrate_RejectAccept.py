#!/usr/bin/python3
'''
!--------------------------------------------------------
! Paradeigma oloklirwsis tis methodou aporipsis 
! xrisimopoiontas tyxaioys arithmoys
! Efarmogi sti synartisi F(x) = x**2*exp(-x).
! Apotelesma einai -(x^2+2x+2)exp(-x)~1.99446
!--------------------------------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

def integrand(x):
    y = x * x * np.exp(-x)
    return y

def MCIntegration_RejectAccept(ntr,XLowLim,XUpLim,Ymax,Ymin):
    Npass = 0
    for i in range(ntr):
        xr = random()
        xrnd = LowLim + (XUpLim-XLowLim)*xr
        yr = random()
        ftest = Ymin + (Ymax - Ymin) * yr
        if (integrand(xrnd) > ftest) :
            Npass = Npass + 1
    A = (Ymax-yYmin)*(XUplim-XLowLim)  # Emvado orthogwniou
    Integral = A * Npass/ntr
    return Integral


ntries = int(input("How many tries to evaluate the integral ? "))
lowlimit = float(input("The low limit of integration "))
hilimit = float(input("The upper limit of integration "))
ymax = float(input("The max value of y "))
ymin = 0
iseed = 123456
seed(iseed)

result = MCIntegration_RejectAccept(ntries,lowlimit,hilimit,ymax,ymin )
print("After %6d tries, the integral is %10.5f"%(ntries,result))

