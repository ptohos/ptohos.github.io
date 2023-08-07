#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, randrange

def random_step(x,y):
    direction = randrange(4)   # 4 dunates kateythunseis
    if direction == 0:
        x = x - 1
    elif direction == 1:
        x = x + 1
    elif direction == 2:
        y = y - 1
    else:
        y = y + 1
    return x, y

#... Main

seed(123456)
mxtime = int(input('Specify the max time of a walk '))
mxwalks = int(input('Specify the max number of walks '))
TheTime = []
TheDist = []

my_file = open('Askisi4.dat','w')
my_file.write('%9s  %12s\n'%('Time','<Distance>'))
for time in range(mxtime):                # Gia oles tis xronikes stigmes
                                          # yparxoun maxwalk diadromes
    distance = 0.     # Initialization tis apostasis
    for iwalk in range(mxwalks):
        xpos = 0      # Stin arxi tis diadromis
        ypos = 0
        for it in range(time):              # Eyresi tis apostasis pou kalupse
            x, y = random_step(xpos,ypos)   # kata tin diadromi ayti to  
            xpos = x                        # sygkekrimeno xroniko diastima
            ypos = y
        distance = distance + np.sqrt(xpos**2 + ypos**2)
    average_dist = distance/mxwalks
    TheTime.append(time)
    TheDist.append(average_dist)
    my_file.write('%5d %8.4f'%(time,average_dist))
    
my_file.close()
plt.figure(figsize=(6,6))
plt.plot(TheTime,TheDist,'oC1-')
plt.xlabel('Time,t(a.u.)')
plt.ylabel(r'$<$Distance$>$,(a.u.)')
plt.title('2d-random walk:<Distance> vs time')
plt.grid(True)
plt.savefig('RandomWalk.pdf')
plt.show()
