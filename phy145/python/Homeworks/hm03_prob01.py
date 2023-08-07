#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

filename=input("Give the filename ")    # inp_integers.dat apo tin 
infile = open(filename,'r')             # askisi 3 tou lab03

FreqDict={}
for line in infile:
    key = int(line.strip())        # To file exei arithmous sto diastima [1,30]
                                   # Anagnwsi twn arithmwn aytwn ws keys 
    FreqDict[key] = FreqDict.get(key,0) + 1

# Taksinomisi twn stoixeiwn tou dictionary
# H parakatw taksinomisi epistrefei a list of tuples
a = list(sorted(FreqDict.items(), key=lambda cnt: (cnt[1],cnt[0])))
# Eksagwgi kathe stoixeiou tou tuple se ksexwristi lista
xval = list(map(lambda x: x[0], a))
yval = list(map(lambda x: x[1], a))

plt.figure(figsize=(7,5))
plt.plot(xval,yval,'bo')             #Oi dyo aksones einai taksinomimenoi me 
plt.title('Frequency of numbers')    #vasi ti syxnotita emfanisis kai etsi an 
plt.xlabel('x')                      #enwsoume ta simeia tha paroume mia 
plt.ylabel('Frequency')              #tethlasmeni grammi
plt.xlim(0,30)

plt.show()
