#!/usr/root/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, gauss

ntries = int(input("How many tries? "))
seed(12345678)
sigma = 15.
mu = 100.
x = []

for i in range(ntries):
    x.append(gauss(mu,sigma))

cont,binv,intr=plt.hist(x,bins=50,range=(0.,200.),density=True,histtype='step')

plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number gaussian distributed')
plt.xlim(40,160)
plt.ylim(0.,0.03)
plt.text(60,0.025,r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.show()

