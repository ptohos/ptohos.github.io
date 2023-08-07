#!/usr/bin/python3

'''
   Prosomoiosi enos tyxaiou peripatoy se mia diastasi
   O peripatitis exei tin idia pithanotita na kinithei
   pros ti mia i tin alli pleura 
'''

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed
ipower = int(input('Give the max power of 10 for MC simulations:'))
dist = int(input('Give the maximum length l: '))
seed(123456)
prob = 0.5       # pithanotita gia vima aristera i deksia
for iw in range(ipower):
    mxwalks = 10**(iw+1)
    totsteps = 0
    for iwalks in range(mxwalks):
        nsteps = 0       # Metritis vimatwn
        x = 0            # Arxiki thesi
        while np.abs(x) < dist :  
            if random() > prob:
                x = x + 1
            else:
                x = x - 1
            nsteps = nsteps + 1
        totsteps = totsteps + nsteps

    avesteps = totsteps/float(mxwalks)
    if iw == 0 :
        print('%10s  %10s' % ('Ntries','Average'))
    print(" %8d  %15.6f" % (mxwalks,avesteps))
