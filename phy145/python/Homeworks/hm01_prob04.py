#!/usr/bin/python3

import numpy as np

epsi  = 1E-6
theta0 = 0.1
for icase in range(4):
    theta = theta0 * 10**icase
    sintheta = np.sin(theta)
    if theta > 2*np.pi:
        x = theta - int(theta/(2*np.pi))*2*np.pi  # Metatropi wste i gwnia na 
    else:                                         # pantote sto diastima [0,2pi]
        x = theta                                 # An to x einai megalo tote
                                                  # odigei se avevaiotita logw
                                                  # sfalmatos apokopis
    suma  = 0.0       # Arxiki timi gia to athroisma
    count = 0.0       # oroi athroismatos
    term  = x
    while abs(term) >= epsi:     # Kathe oros tou athroismatos prokuptei apo ton
        suma  = suma + term      # proigoumeno pol/zontas -x^2/[(2*i)*(2*i+1)]
        count = count + 1        # p.x i=1 (-1)*x^3/3! diladi -x * x^2/(2*3)
                                 #     i=2 x^5/5! diladi x^3/(2*3) * x^2/(4*5)
                                 #                        i=1 oros        
        term  = -term * x**2/((2*count+1)*(2*count))
    if icase == 0:
        print('============== Apotelesmata ===============')
        print(' theta     sin(x)    sin(x) from Sum  oroi')
    print('%5.1f %12.6f %12.6f %8d'%(theta,sintheta,suma,count))
print('==========================================')
