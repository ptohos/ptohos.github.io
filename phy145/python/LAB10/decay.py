#!/usr/bin/python3

from random import random
import numpy as np
import matplotlib.pyplot as plt

# Statheres

NA0 = 1000    # arxikoi astatheis purines
NA = NA0
NB = 0        # arxikoi staatheroi pirines
tau = 3.053*60 # xronos imiseias zwis
dt = 1.0      # xroniko vima

p = 1 - np.exp(-dt/tau)  # pithanotita diaspasis se ena xroniko vima
tmax = 1000      # sunolikos xronos gia tin prosomoiwsi

# Grafimata
tpoints = np.arange(0.0,tmax,dt)
theory=[]
theory = NA0*np.exp(-tpoints/tau)
TApoints = []
TBpoints = []

# Main program
for t in tpoints:
    TApoints.append(NA)
    TBpoints.append(NB)

    # Oi purines poy diaspastikan
    decay = 0
    for i in range(NA):
        if random() < p :
            decay += 1
    NA = NA - decay
    NB = NB + decay

plt.plot(tpoints,TApoints,label="Unstable nuclei A")
plt.plot(tpoints,TBpoints,label="Stable nuclei B")
plt.plot(tpoints,theory,'g--',label="Exponential decay")
plt.xlabel("Time")
plt.ylabel("Number of nuclei")
plt.title("Decay of unstable nuclei",size=14)
plt.legend()
plt.xlim(0,tmax)
plt.ylim(0,1.1*NA0)
plt.show()
