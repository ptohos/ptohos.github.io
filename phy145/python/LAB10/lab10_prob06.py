#!/usr/bin/python3

'''
  Efarmogi tis methodou aporripsis timwn
  gia kataskeyi tyxaiwn arithmwn pou 
  katanemontai symfwna me kapoia 
  puknotita pithanotitas PDF
  H sunartisi pou dinetai xreiazetai na 
  kanonikopoiithei sti monada. 
  H PDF synartisi einai mia gaussian
        A*exp[-(x-mean)^2/2sigma^2]
  opou mean = 0 kai 2*sigma^2 = 1 =>sigma=sqrt(2)/2
  O Paragontas kanonikopoiisis A einai 
  A = 1/[sqrt(2*pi)*sigma] wste to oloklirwma tis 
  sunartisis na einai 1.  
'''
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

def PDF(x):
    return np.exp(-x*x)

def find_max(func,xlo_lim,xup_lim):
    fmax = -9.0E9
    mctries = 1000000
    for itry in range(mctries):
        x = xlo_lim + (xup_lim - xlo_lim)*random()
        y = func(x)
        if y > fmax:
            fmax = y
    return fmax


#....Main

xminv = float(input('Lower x-limit '))
xmaxv = float(input('Upper x-limit '))
mxtries = int(input('How many random numbers? '))
xvalues = np.array([xminv,xmaxv])
seed(1234567)

ymax = find_max(PDF,xminv,xmaxv)
xvrnd = []
condition=True
ntries = 0
while condition:
    ntries += 1
    xr = xminv + (xmaxv - xminv) * random()
    yr = ymax * random()     # Epilogi enos tyxaiou y sto diastima [0,ymax]
    y  = PDF(xr)             # Eyresi tis timis tis PDF gia to x pou epilexthike
    if yr < y:               # to zeygari (xr,yr) einai katw apo tin timi tis 
                             # PDF(xr) opote epilegetai
        xvrnd.append(xr)
    length = len(xvrnd)
    if length >= mxtries:    
        condition = False

print('\n %6d Random numbers generated after %8d tries\n' % (mxtries,ntries))
plt.figure(figsize=(6,6))
cont,xbinval,intr=plt.hist(xvrnd,bins=100,range=(-5.,5.),density=True,
                           histtype='step',color='g')
norm=np.sqrt(2*np.pi)*np.sqrt(2)/2
ypdf=PDF(xbinval)/norm
plt.plot(xbinval,ypdf,'b-',label=r'PDF: $e^{-x^2}$')
plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number distributed according to $e^{-x^2}$')
plt.axis([-5,5.,0,0.6])
plt.grid(True)
plt.legend()
plt.show()
