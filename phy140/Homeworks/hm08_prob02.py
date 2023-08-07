#!/usr/bin/python3

import sys
import random
from random import seed
from math import sqrt
import matplotlib.pyplot as plt

N = int(input("How many numbers to draw ? "))
sum   = 0.0
sumsq = 0.0

seed(12345)
xval, yval, syval = [],[],[]
for itry in range(1,N+1):
    x = random.uniform(-3, 3)
    sum += x
    sumsq += x*x

    if itry % (N/10) == 0:
        xmean = sum/itry
        stdev = sqrt(sumsq/itry - xmean*xmean)
        print(" %8d mean: %12.5e stdev: %12.5e" %(itry, xmean, stdev))
        xval += [itry]
        yval += [xmean]
        syval+= [stdev]
print("Standard deviation form MC :",stdev)
print("Theoretical deviation: ",6/sqrt(12))
        
plt.figure(figsize=(8,5))
plt.subplot(1,2,1)
plt.plot(xval,yval,'bo',linestyle='-')
plt.xlabel('x')
plt.ylabel('$x_{mean}$')
plt.ylim(-0.2,0.2)
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(xval,syval,'bo',linestyle='-')
plt.ylim(1.2,1.8)
plt.xlabel('x')
plt.ylabel('$x_{std}$')
plt.grid(True)
plt.tight_layout()
plt.show()
