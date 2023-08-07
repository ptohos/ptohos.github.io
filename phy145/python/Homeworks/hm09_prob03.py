#!/usr/bin/python3

'''==========================================================================
   Prosomoiwsi tis radienergous diaspasis
   duo radienergwn purinwn o enas ek twn 
   opoiwn apotelei proion tou allou.
   H theoritiki lusi einai:
   
   NA(t) = NA(t=0) * exp(-L_A*t)     opou L_A = omega_A = 1/tau_A
   NB(t) = [ NA(t=0) * L_A/(L_B - L_A) ] * [ exp(-L_A*t) - exp(-L_B*t) ] + 
         +   NB(t=0) * exp(-L_B*t)

   H prosomoiwsi isxyei gia tis periptwseis pou omega*t << 1

   Ws paradeigma tha xrisimopoiisoume: 
       omega_x = 0.01
       omega_y =  omega_x/5 = 0.002  O xronos zwis Y einai 5 fores tou X
       NX      = 1000
       NY      =    0
       tmax    = 1000
       dt      =    1
       Ntries  = 10000

  H diadikasia ekteleite Ntries wste na paroume ti mesi timi se kathe 
  xroniko vima apo polla peiramata wste na exoume gia kathe xroniki stigmi 
  ena kalo deigma kai na apofeuxthoun statistikes diakumanseis
 =========================================================================='''

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed


N0X = int(input("Enter the initial number of X nuclei [N0X = 1000] "))
N0Y = int(input("Enter the initial number of Y nuclei [N0Y =    0] "))
omegaX = float(input("Enter the decay constant of X nuclei [1/tau_X = 0.01] "))
omegaY = float(input("Enter the decay constant of Y nuclei [1/tau_Y = 0.002] "))
tmax   = float(input("Enter the total time for the simulation [tmax = 1000] "))
dt     = float(input("Enter the time step [dt = 1s] "))
MxTries= int(input("Enter the number of experiments to perform [MxTries = 10k] "))

seed(123456)

Ntot_NX = []
Ntot_NY = []
NX_theory = []
NY_theory = []

for itry in range(MxTries):
    ''' Gia kathe prosomoiwsi ksekiname apo tis arxikes synthikes '''
    NX_left = N0X
    NY_left = N0Y
    t_elapsed = 0.
    ktime = 0
    try:     # Kratame statistiki gia kathe xroniki stigmi gia kathe prosomoiwsi
        Ntot_NX[ktime] += NX_left
        Ntot_NY[ktime] += NY_left
    except:  # Stin proti prosomoiwsi gemizoume tin list
        Ntot_NX.append(NX_left)
        Ntot_NY.append(NY_left)
        NX_theory.append(N0X)
        NY_theory.append(N0Y)
    doit = True
    while doit:
        ktime += 1
        t_elapsed += dt
        ''' ========================
            Theoritikos upologismos 
            ======================== '''
        if itry == 0:
            X_pirines = int( N0X * np.exp(-omegaX * t_elapsed) )
            NX_theory.append(X_pirines)
            Coeff = N0X * omegaX/(omegaY - omegaX)
            term  = np.exp(-omegaX * t_elapsed) - np.exp(-omegaY * t_elapsed)
            Y_pirines = int( Coeff * term + N0Y * np.exp(-omegaY * t_elapsed))
            NY_theory.append(Y_pirines)
        ''' =========================
            Prosomoiosi - 
            Posoi purines diaspontai se kathe xroniki stigmi
            ========================= '''
        nx = NX_left
        for inucl in range(nx):
            r = random()
            if r < omegaX :     # Eksetasi an o X purinas diaspatai
                NX_left -= 1    # Elatonoume tous X purines kata 1
                NY_left += 1    # Auksanoume tous Y purines kata 1
        ny = NY_left
        for inucl in range(ny): # Ekseta an o Y pyrinas diaspatai
            r = random()
            if r < omegaY :
                NY_left -= 1
        '''=================================
           Apothikeusi apotelesmatwn 
           gia to sygkekrimeno xroniko vima
           ================================='''
        try:
            Ntot_NX[ktime] += NX_left    
            Ntot_NY[ktime] += NY_left
        except:
            Ntot_NX.append(NX_left)   # Tin prwti fora
            Ntot_NY.append(NY_left)
        '''====================================
           Elegxos gia to fthasame sto megisto
           xroniko orio tis prosomoiosis 
           ===================================='''
        if t_elapsed >= tmax:
            doit = False
Time=[]
for ktime in range(len(Ntot_NX)):
    Time.append(ktime*dt)
    Ntot_NX[ktime] = int(Ntot_NX[ktime]/MxTries)
    Ntot_NY[ktime] = int(Ntot_NY[ktime]/MxTries)

plt.figure(figsize=(7,5))
plt.plot(Time,Ntot_NX,'bo',markersize=2,label='X-purines')
plt.plot(Time,NX_theory,'r--',linewidth=2)
plt.plot(Time,Ntot_NY,'r^',markersize=2,label='Y-purines')
plt.plot(Time,NY_theory,'b--',linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("No. of nuclei")
plt.legend()
plt.ylim(0,1050)
plt.xlim(0,1001)
plt.grid(True)
plt.show()

