#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed, randrange

def throw(n):
    sum = 0
    for i in range(n):
        side = 1 + randrange(6)
        sum += side
    return sum

#... Main

nzaria = int(input('Arithmos zariwn se kathe ripsi [2]: '))
nripseis = int(input('Arithmos ripsewn twn zariwn [10000]: '))
#
seed(123456)
res1 = []
res2 = []
#
for iripseis in range(nripseis):
    res1.append(throw(nzaria))
    res2.append(throw(nzaria+1))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
cont,binval,intr = plt.hist(res1, bins=13, range=(-0.5,12.5), histtype='step')
plt.xlabel('Athroisma')
plt.ylabel('Plithos')
plt.title('Athroisma apo ripseis %d zariwn'%nzaria) 
plt.text(2.1,1500,r'%d prospatheies'%nripseis)
plt.xlim(1.5,12.5)
plt.grid(True)

plt.subplot(1,2,2)
content,binva,intr=plt.hist(res2, bins=19, range=(-0.5,18.5), histtype='step')
plt.xlabel('Athroisma')
plt.ylabel('Plithos')
plt.title('Athroisma apo ripseis %d zariwn'%(nzaria+1)) 
plt.text(4,1200,r'%d prospatheies'%nripseis)
plt.xlim(2.5,18.5)
plt.grid(True)
#
plt.tight_layout()
#
plt.savefig("hm08_prob06.pdf")
#
plt.show()
