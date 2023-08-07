#!/usr/bin/python3

'''=========================================
   To programma prosomoiwnei tin arxi
   elaxistis diadromis tou fwtos (arxi
   tou Fermat) otan ayto perna apo ena 
   meso me deikti diathlasis n1 se allo
   meso me deikti diathlasis n2
   Ta duo mesa xwrizontai me mia epifaneia.

   Theoroume oti exoyme Nmax ylika mesa
   pou xwrizontai me Nmax-1 epifaneies 
   ========================================='''

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, randint

def initialize(N):
    ypos = np.zeros(N+1)
    vel  = np.ones(N)
    n1 = 1.0       # Deiktis diathlasis tou mesou 1
    v1 = 1/n1      # Taxytita toy fwtos sto meso 1
    n2 = 1.5       # Deiktis diathlasis tou mesou 2
    v2 = 1/n2      # Taxytita tou fwtos sto meso 2
    for j in range(int(N/2)):
        vel[j] = v1          # Taxytita tou fwtos sto prwto miso
    for j in range(int(N/2),N):  
        vel[j] = v2          # Taxytita tou fwtos sto deutero miso 
    ypos[0]   = 2            # Thesi tis pigis tou fwtos
    ypos[N]   = 8            # Thesi tou anixneyti

    ''' Epilogi tyxaiwn simeiwn kata mikos tis y-dieythunsis gia tin
        arxiki tyxaia diadromi apo tin pigi sto simeio anixneusis'''
    for j in range(1, N):
        ypos[j] = (ypos[N] - ypos[0])*random() + ypos[0]
    return ypos, vel

def change_path(y,v,N, MxTries):

    delta = 0.5    # Megisti epitrepomeni allagi sti y-thesi panw stin epifaneia

    for itries in range(MxTries):
        x = randint(1,N-1)                      # Epilogi tuxaias epifaneias
                                                # Oi diaxwristikes epifaneies
                                                # einai x=1,2,...,N-2
                                                # enw x=0,x=N-1 einai i pigi
                                                # kai to simeio anixneusis
        ''' Eyresi tou xronou ptisis apo to simeio tis diadromis stin 
            proigoumeni epifaneia mexri to simeio tis diadromis stin epomeni 
            epifaneia''' 
        dysq = (y[x] - y[x+1])*(y[x] - y[x+1])  # Katheti apostasi tou arxikou
        dist = np.sqrt(1+dysq)                  # simeiou stin epifaneia x apo
                                                # ayto stin epomeni epifaneia
        t_org = dist/v[x]                       # Xronos ptisis gia dist
        dysq = (y[x] - y[x-1])*(y[x] - y[x-1])
        dist = np.sqrt(1+dysq)                  # Apostasi apo to simeio tis
                                                # proigoumenis epifaneias
        t_org += dist/v[x-1]                    # Synolikos xronos ptisis
        ''' Epanalipsi tis idias diadikasias xrisimopoiontas twra to 
            neo simeio tis diadromis stin epilegmeni epifaneia '''
        ytest = y[x] + (2*random() - 1)*delta   # nea y-thesi gia to fws stin
                                                # sygkekrimeni epifaneia
        dysq = (ytest - y[x+1])*(ytest-y[x+1])
        dist = np.sqrt(1+dysq)
        t_test = dist/v[x]
        dysq = (ytest - y[x-1])*(ytest-y[x-1])
        dist = np.sqrt(1+dysq)
        t_test += dist/v[x-1]
        if t_test < t_org :                     # Me to neo simeio i diadromi
            y[x] = ytest                        # einai pio grigori

def main():
    seed(12345)
    N = int(input("Enter the number of different media "))
    NMxTries = int(input("Enter the number of tries "))
    y,velocity = initialize(N)
    yint = np.zeros(N+1)
    for i in range(N+1):
        yint[i] = y[i]
    change_path(y,velocity,N,NMxTries)
    xpos = np.arange(N+1)

    plt.figure(figsize=(7,5))
    plt.plot(xpos,yint,'r:',label='Arxiki diadromi')
    plt.plot(xpos,y,'b-',label='Fermat diadromi')
    plt.xlim(-0.5,N+0.5)
    plt.ylim(0,10)
    plt.xlabel('xposition (m)')
    plt.ylabel('yposition (m)')
    plt.text(-0.2,1.7,'source')
    plt.text(9.5,8.1,'detector')
    for j in range(1,N):
        plt.axvline(j,0,10,linestyle=':')
        if j == int(N/2):
            plt.axvline(j,0,10,color='g',lw=4)
    plt.legend()
    plt.grid(True)
    plt.show()

main()

    
