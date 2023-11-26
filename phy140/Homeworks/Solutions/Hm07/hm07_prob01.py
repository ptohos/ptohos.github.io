#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

seed(123456)

NMC = int(input("Give the number of MC to try: "))
nused = 0
numb_list = []
for itry in range(NMC):
    doit = True
    sum  = 0
    numb = 0
    while doit:
        x = random()
        numb += 1
        sum += x
        if sum > 1:
            doit = False
    nused += numb
    numb_list += [numb]
ave_numb = float(nused)/NMC
print("Average number of random numbers used to have a sum > 1 is %10.9f"%ave_numb)
print("Expected number of random numbers used to have a sum > 1 is %10.9f "%np.exp(1))


const, binv, intr = plt.hist(numb_list,bins=10,range=(0.5,10.5),density=True,histtype='step')
plt.xlabel("Number of terms in the sum")
plt.ylabel("Probability density function, (PDF)")
plt.xlim(0,11)
#plt.ylim(0,1.)
plt.grid(True)
plt.show()
