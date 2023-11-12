#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, expovariate

ntries = int(input("How many tries? "))
nbins = 100
xlimit = 10.
seed(12345678)
lamb=0.8
x = []

for i in range(ntries):
    x.append(expovariate(lamb))
             
plt.figure(figsize=(8,8))

plt.subplot(2,2,1)
cont,binv,intr=plt.hist(x,bins=nbins,range=(0.,xlimit),density=None,histtype='step')
plt.xlabel('x-values')
plt.ylabel('Frequency of appearance')
#plt.title('Random number distributed exponentially')
plt.xlim(0,xlimit)
plt.ylim(0.,80000)
plt.grid(True)
# PDF
plt.subplot(2,2,3)
pcont,binv,intr=plt.hist(x,bins=nbins,range=(0.,xlimit),density=True,histtype='step')
plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.xlim(0,xlimit)
plt.ylim(0.,0.8)
plt.grid(True)
#
xval = []
sumcont=[]
sumnorm=[]
count = 0
norm  = 0
binsz = (binv[-1]-binv[0])/nbins
suma = sum(cont)
sump = sum(pcont)
for i in range(len(cont)):
    count   += cont[i]/suma
    norm    += pcont[i]/sump   #>> Cummulative 
    sumcont += [count]
    sumnorm += [norm]
    xval    += [binv[i]+binsz/2]
plt.subplot(2,2,2)
plt.plot(xval,sumcont)
plt.xlim(0.,xlimit)
plt.xlabel("x-values")
plt.ylabel("Cumulative Distribution Function,CDF")
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(xval,sumnorm)
plt.xlim(0.,xlimit)
plt.xlabel("x-values")
plt.ylabel("Cumulative Distribution Function,CDF")
plt.grid(True)
plt.tight_layout()
plt.show()
