#!/usr/bin/python3
'''
 Monte Carlo gia proseggisi tis ripsis toy nomismatos 6 fores!
 To nomisma rixnetai 6 fores. 
 To programma upologizei tin pithanotita na paroume:

  (a)   akribws 4 fores heads
  (b)   toulaxiston 4 fores heads 

  xrisimopoiei ti Methodo Monte Carlo gia difforetiko plithos
 prospatheiwn. Ta analytika apotelesmata einai:

  (a) 0.234375
  (b) 0.34375
'''

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

iseed = 123456
seed(iseed)

for i in range(7):            # 10, 100, ..., 10^ peiramata
    i=i+1
    N = 10**i                 # Plithos peiramatwn
    E4H  = 0                  # Akribws Heads
    AL4H = 0                  # Toylaxiston 4 Heads
    
    for j in range(N):        # N peiramata me 6 ripseis
        Head = 0              # Gia kathe peirama 6 ripsewn
                              # midenizoume ton arithmo twn epituximenwn ripsewn
        for k in range(6):    # 6 ripseis tou nomismatos
            R = random()
            if R >= 0.5: Head = Head + 1.
        if Head == 4:  E4H = E4H  + 1.
        if Head >= 4: AL4H = AL4H + 1.
            
    print(N,E4H/N,AL4H/N)


