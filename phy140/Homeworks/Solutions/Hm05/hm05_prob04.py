#!/usr/bin/python3
'''
=============================================================
 H eyresi tou simeiou lagrange metaksu Gis-Selinis wste na
 exoume sto simeio ayto tin idia periodo peristrofis me 
 ayti ti Selinis vrisketai me to na lusoume tin eksiswsi
 pou dinetai stin askisi. Ayti einai mia eksiswsi 5ou
 bathmou. Epomenws mporoume na xrisimopoiisoume mia apo
 tis methodous euresis rizas (newton,bisection)
============================================================='''
import numpy as np

def func(R,GMg, GMs, Rgs, omg):
    result = GMg/(R*R) - GMs/(Rgs-R)**2 - R*omg*omg
    return result

def deriv(R,GMg, GMs, Rgs, omg):
    result = -2.0*GMg/(R*R*R) - 2.0*GMs/(Rgs-R)**3 - omg*omg
    return result

precision=float(input("Give the desired precision "))
G = 6.675E-11      # gravitational constant
Mearth = 5.974E24  # mass of earth
Mmoon  = 7.348E22  # mass of moon
omega  = 2.662E-6  # omega
R_em   = 3.844E8   # radius of earth
GMea   = G*Mearth
GMmo   = G*Mmoon

R = R_em/2       # First choice for solution

error = func(R,GMea,GMmo,R_em,omega)/deriv(R,GMea,GMmo,R_em,omega)
while abs(error) > precision:
    R = R - error
    error = func(R,GMea,GMmo,R_em,omega)/deriv(R,GMea,GMmo,R_em,omega)
print(' To simeio Lagrange vrisketai se apostasi %10.5g' % R)

