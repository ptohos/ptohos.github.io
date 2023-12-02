#!/usr/root/python3
'''
  Dimiourgia tyxaiwn arithmwn pou katanemontai 
  symfwna me tin ekthetiki sunartisi exp(bx)
  opoy o paragontas b einai > 0 
'''
import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, gauss

def myfunc(numb):
    return np.exp(rate*numb)

ntries = int(input("How many tries? "))
seed(12345678)

x =[]
rate = 1
uplim = 2
lolim = 1
norm = 1/np.abs(np.exp(uplim) - np.exp(lolim))
pdf = []
for i in range(ntries):
    x.append(np.log(np.exp(lolim) + random()/(rate*norm)))

cont,xbinval,intr=plt.hist(x,bins=20,range=(1.,2.),density=True,
                           histtype='step',color='g')

pdf=norm*np.exp(rate*xbinval)
plt.plot(xbinval,pdf,'b-',label='Theoretical PDF')
plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number exponentially distributed in the range [1,2]')
plt.axis([0,4.,0,1.6])
plt.text(3,1.30,r'$P(y)=e^{\lambda x},\ \lambda=1$')
plt.grid(True)
plt.legend()
plt.show()
