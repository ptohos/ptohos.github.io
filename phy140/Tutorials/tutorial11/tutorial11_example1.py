#!/usr/bin/python3
'''
 Eyresi tis timis tou pi me ti methodo Monte Carlo

 Orizoume ena parallilogrammo me mikos pleuras a=3 kai b=2,
 to opoio perikleiei to ena tetartimorio tis elleipsis.
 To embado tou parallilogrammou einai a*b. 
 Epilegoume tyxaia simeia x sto diastima [0,3] kai y sto 
 diastima [0,2] ta opoia zitoume na ikanopoioun tin eksiswsi
 tis elleipsis x**2/a**2 + y**2/b**2 <= 1. 
 To embado tis elleipsis tha einai tote: E = a * b * N_ellipsi/Ntot
'''

import numpy as np
from random import seed, random

a    = 3.0
b    = 2.0
R_el = 1.0

seed(1234567)

for j in range(7):
    N_tot = 10**(j+1)
    N_pass = 0
    if j == 0:
        print("%11s %14s %14s %12s %15s"%
              ("Ntries","Area ala MC", "Area Theory","Diafora", "Timi tou pi"))
    for itry in range(N_tot):
        xrand = a*random()
        yrand = b*random()
        ellip = xrand**2/a**2 + yrand**2/b**2
        if ellip <= R_el**2 : N_pass += 1
    integral = N_pass/N_tot
    Area_MC  = 4 * integral * a * b
    Area_theory = np.pi * a * b
    print("%10i %14.6f %14.6f %14.7f %13.7f"%
          (N_tot,Area_MC, Area_theory, abs(Area_MC-Area_theory), 4*integral))
