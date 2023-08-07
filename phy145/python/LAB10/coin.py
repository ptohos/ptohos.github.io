#!/usr/bin/python3

import numpy as np
from random import random, seed


ntries = int(input("How many tries? "))

probability = .5  # for heads or tail
nHeads = 0
nTails = 0

# Ektelesi peiramatwn ripsis tou nomismatos
for itries in range(ntries):
    p = random()
    if p < probability:
        nHeads += 1.
    else:
        nTails += 1.
        
print("probability is set to ", probability)
print("Head Count: ", nHeads)
print("Tail Count: ", nTails)
print("Probability after {0:d} random numbers = {1:6.4F}% ".format(ntries,nHeads*100/ntries)) 
