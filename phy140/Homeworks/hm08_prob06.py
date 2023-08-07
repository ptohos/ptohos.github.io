#!/usr/bin/python3

import numpy as np
from random import seed, random, randint

seed(123456)

mxtries = int(input("Enter the number of tries "))

success = 0

for itry in range(mxtries):
    thesi = 4                #Arxiki thesi
    while (thesi == 4 or thesi == 5 or thesi == 8 or thesi == 9) :
        r = random()
        if r < 0.25 :
            thesi = thesi - 1
        elif r < 0.50:
            if thesi < 6:
                thesi = thesi - 3
            else:
                thesi = thesi - 4
        elif r < 0.75:
            thesi = thesi + 1
        else:
            if thesi < 6:
                thesi = thesi + 4
            else:
                thesi = thesi + 3
        if thesi == 10 or thesi == 11:
            success +=1
            
pithanotita = success*100/mxtries
print("Meta apo %d prospatheies i pithanotita na vrethei se bar einai %5.2f%s)"% (mxtries,pithanotita,"%"))

