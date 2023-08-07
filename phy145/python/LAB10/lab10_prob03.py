#!/usr/bin/python3

"""
This module estimates pi by simulating a dart throw game.
A large number of darts are thrown at a square with vertices
(1,-1), (1,1),(-1,1) and (-1,-1).  The darts land anywhere
in the square with equal probability. If the dart lands inside
the unit circle we call that a "hit". For a large number of throws
N, the the ratio of hits to throws should approximately equal
the ratio of the area of the circle to the area of the square.
Thus pi/4 should approximately equal hits/N.
"""

# What we need from the standard module random
from random import random, seed

#Ntries = int(input("Number of tries ? "))
seed(123456)  # For repeatability of experiments
cases=[100,1000,5000]
print("\n    Total number of throws \t pi Estimate")
for Ntries in cases:
    Hits = 0
    for throws in range(Ntries):
        # Generate and check the k-th dart throw
        x = -1.0 + 2.0*random()    # metasximatismos sto diastima [-1, 1)
        y = -1.0 + 2.0*random()
        if x*x + y*y <= 1:         # mesa ston kuklo 
            Hits += 1
            piEst = 4 * (float(Hits) / float(Ntries))
    print("\t %6d \t\t %10.7f"% (Ntries,piEst))
