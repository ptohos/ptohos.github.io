#!/usr/bin/python3

'''
Lysi tis diaforikis eksiswsis fortisis enos pyknwti
Theoroyme oti o puknwtis exei xwritikotita C kai vrisketai
arxika me mideniko fortio Q0. Arxizei na fortizetai mesw 
antistasis R kai pigis dunamikou Vo. Meta apo xrono t exei
dunamiko V. H diaforiki eksiswsi einai: 
  Vc + IR = Vp => Vc = Vp-IR => Vc = Vp-R*dQ/dt => Q/C = Vp - R*dQ/dt =>
  => dQ/dt = -Q/RC + Vp/R = 
H theoritiki lusi  Q = Qo[1- exp(-t/RC)]
'''

import numpy as np
import matplotlib.pyplot as plt

def deriv(RC,t,Q) :
    return Vp/R - Q/(RC)

dt=[]
ntries = int(input("Give the number of different steps to try "))
for i in range(ntries):
    form = "Give the time step for the %.d try "%(i+1) 
    dt1 = float(input(form))
    dt.append(dt1)

Vp     = 12         # Dunamiko pigis
Vo     = 0          # arxiko voltage piknwti
C      = 1e-6       # 1uF
R      = 1000   
t0     = 0
RC     = R*C
tmax   = 4*RC       # 1 msec = RC 
Qo     = C*Vo
theory = []
comm = ['r--', 'm--']
leg  = ['dt=1E-5','dt=1E-6']

for i in range(ntries):
    time, charge, der, voltage = [],[],[], []
    t = t0           # Arxikopoiisi twn arxikwn timwn gia kathe dt
    Q = Qo
    V = Q/C
    while t <= tmax :
        if i == 0: theory.append(Vp * ( 1.0 - np.exp(-t/RC) ) )
        dqdt = deriv(RC,t,Q)
        time.append(t)
        charge.append(Q)
        voltage.append(V)
        der.append(dqdt)
        Q = Q + dqdt*dt[i]
        V = Q / C
        t = t + dt[i]

    if i == 0:
        plt.plot(time,theory,'b-',label="Analytiki lusi")
        plt.plot(time,voltage,comm[i],label=leg[i])

    del time
    del charge
    del voltage
    del der

plt.title("Charging of a capacitor",size=16)
plt.xlabel("Time,t (ms)")
plt.ylabel("Voltage,V(V)")
plt.xticks(np.linspace(0,tmax,5)) # kathorismos ypodiairesewn ston x-axis
plt.legend()
plt.show()
