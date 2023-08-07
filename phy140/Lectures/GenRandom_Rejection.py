#!/usr/bin/python3

'''
  Efarmogi tis methodou aporripsis timwn
  gia kataskeyi tyxaiwn arithmwn pou 
  katanemontai symfwna me kapoia 
  sunartisi pithanotitas PF i opoia
  den xreiazetai na einai kanonikopoiimeni
  diladi to oloklirwma tis na einai 1.
  Prepei omws i sunartisi na min einai
  arnitiki sto diastima endiaferntos
'''
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

def PDF(x):
    return x**2*np.exp(-x)

def find_max(func,xlo_lim,xup_lim):
    fmax = -9.0E9
    mctries = 1000000
    for itry in range(mctries):
        x = xlo_lim + (xup_lim - xlo_lim)*random()
        y = func(x)
        if y > fmax:
            fmax = y
    return fmax

def MCIntegrate_MeanValue(func,xlo_lim,xup_lim):
    sum = 0.
    mctries = 1000000
    for i in range(mctries):
        xrnd = xlo_lim + (xup_lim - xlo_lim)*random()
        yrvs = func(xrnd)
        sum  += yrvs
    mean_value = sum/mctries
    result = mean_value * (xup_lim - xlo_lim)
    return result

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
cont,xbinval,intr=plt.hist(xvrnd,bins=100,range=(xminv,xmaxv),density=True,
                           histtype='step',color='g')
''' Gia na epivevaisoume oti ontws i katanomi twn tyxaiwn arithmwn einai
    ayti poy antistoixei stin PF pou xisimopoiisame kai epeidi sto
    histogram pernoume tin kanonikopoiimeni PDF tha prepei na
    kanonikopoiisoume tin PF wste na exoume tin PDF kai to oloklirwma tis
    na einai 1 '''
Norm = MCIntegrate_MeanValue(PDF,xminv,xmaxv)
plt.plot(xbinval,PDF(xbinval)/Norm,'b-')
plt.xlabel('x-values')
plt.ylabel('probability function, (PF)')
plt.title('Random number distributed according to $x^2e^{-x}$')
plt.xlim([xminv,xmaxv])
plt.grid(True)
plt.legend()
plt.show()
