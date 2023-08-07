#!/usr/bin/python3

import numpy as np
from random import seed, random, randint

seed(123456)

Ntries = int(input("How many tries "))

Nsuccess = 0
for itry in range(Ntries):
    iz = [randint(1,6) for k in range(3)]  # Treis ripseis zariwn 
    match = 0
    for i in range(len(iz)-1):
        for j in range(i+1,len(iz)):
            if iz[i] == iz[j]:
                match +=1
    
    if match == 1:
        Nsuccess +=1

print(" The simulated probability is %6.4f:" 
      "\n The expected probability is %6.4f:"
      %(Nsuccess*100/Ntries,5*100/12))

      
