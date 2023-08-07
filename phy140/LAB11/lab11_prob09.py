#!/usr/bin/python3

import numpy as np
from random import randint, seed
import matplotlib.pyplot as plt

def fact(N):
    result = 1
    for j in range(N,1,-1):
        result *= j
    return result

def analytical(NPass, Ntot):
    '''Calculation of the binomial probability to get
       npass successes out of ntot tries'''
    SuccessProb = 1/6
    FailProb = 1 - SuccessProb
    NFail = Ntot - NPass
    theory = fact(Ntot)/fact(NPass)/fact(NFail)
    theory = theory * SuccessProb**NPass * FailProb**NFail
    return theory


seed(123456)
Nzaria = int(input("Enter the number of dice "))
Ntries = int(input("Max number of tries "))

Occup = np.arange(Nzaria+1)  # This array will contain the number of occurances
Occup = np.zeros(Nzaria+1)   # of a specific side when rolling Nzaria. We need
                             # to cover all possible 11 outcomes:
                             # 0 out of 10 to 10 out of 10 dices 

for itries in range(Ntries):
    nsuccess = 0
    for izari in range(Nzaria):
        idraw = randint(1,6)
        if idraw == 6:
            nsuccess += 1
    Occup[nsuccess] += 1

print("Draws  Occurances  Ntries   Prob(MC)   Proc(anal.)")
for j in range(Nzaria+1):
    print(' %2d  %10d  %8d  %9.5f  %9.5f'%(j,Occup[j],Ntries,Occup[j]*100/Ntries,100*analytical(j,Nzaria)))

xv =np.arange(0,11)
plt.figure(figsize=(6,4))
plt.bar(xv,Occup,color='b')
plt.xlim(-0.5,10.5)
plt.xlabel('No ziaria')
plt.ylabel('Suxnotita')
imax = max(Occup)
plt.text(4,imax,r'Rolling of %2d dice'%Nzaria)
plt.grid(True)
plt.show()


