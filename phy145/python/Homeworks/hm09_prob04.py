#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed

seed(12345)

# Orismos tou plegmatos tou random walk
xuplim = 8
xlolim = 1
yuplim = 8
ylolim = 1

dist = 0
nwalks = int(input('Give the maximum number of walks [n=5000] '))  
maxsteps = 1
minsteps = 1

for iwalk in range(nwalks):
    xpos = xuplim   # x-coordinate tou simeiou ekkinisis
    ypos = yuplim   # y-coordinate tou simeiou ekkinisis
    nstp = 0
    done = False

    while not done:
        r = random()    
        nstp += 1               # Ayksisi tou metriti vimatwn 
        if r > 0.75:
            xpos = xpos + 1     # kinisi sta deksia tou plegmatos
        elif r > 0.50:
            xpos = xpos - 1     # kinisi sta aristera tou plegmatos
        elif r > 0.25:
            ypos = ypos + 1     # kinisi pros ta panw 
        else:
            ypos = ypos - 1     # kinisi pros ta katw
        ''' =============================================
            Elegxos an to vima pou tha ektelesei fernei
            to swma ektos twn oriwn tou plegmatis. An 
            einai ektos twn oriwn tote epistrefoume stin
            proigoumeni thesi kai elattwnoume ton arithmo
            twn vimatwn kata 1 kai dokimazoume nea vima
            ============================================='''
        if xpos > xuplim:
            xpos -= 1
            nstp -= 1
        elif ypos > yuplim:
            ypos -= 1
            nstp -= 1
        elif xpos < xlolim:
            xpos += 1
            nstp -= 1
        elif ypos < ylolim:
            ypos += 1
            nstp -= 1
        else:
            pass
            
        if xpos == xlolim and ypos == ylolim:
            done = True
    '''=========================
       Eyresi tou megistou kai 
       elaxistou arithmou vimatwn
       =========================='''
    if iwalk == 1:
        maxsteps = nstp
        minsteps = nstp
    elif maxsteps < nstp:
        maxsteps = nstp
    elif minsteps > nstp:
        minsteps = nstp
    else:
        pass
    
    dist += nstp      # Athroisma tou arithmou twn vimatwn kathe diadromis 

print('============ Apotelesmata meta apo %d diadromes ==============='%nwalks)
print('Diadromi me megisto arithmo vimatwn: %d' % maxsteps)
print('Diadromi me elaxisto arithmo vimatwn: %d' % minsteps)
print('Mesi timi diadromis: %8.3f' % (dist/nwalks))
print(65*'=')
