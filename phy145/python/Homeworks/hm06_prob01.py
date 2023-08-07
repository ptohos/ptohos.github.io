#!/usr/bin/python3

'''===================================================================
... To programma ayto lunei to problima tis ekseliksis tis mazas
... tou alatiou se kapoio dialuma. Sumfwna me to problima mia 
... statheri posotita dialumatos feygei apo to doxeio pou to
... periexei enw i idia posotita dialuti prostithetai me ton idio
... ruthmo.  Sti prokeimeni periptwsi to dialuma to opoio
... apomakrunetai apo to doxeio me kapoio stathero rythmo exei
... tin idia puknotita me tin piknotita tou doxeiou. Epomenws an
... upothesoume oti i maza tou alatious se kathe xroniki stigmi 
... einai S(t) (sunartisi tis xronikis stigmis t) i diaforiki
... eksiswsi pou tha perigrafei ti metavoli tis posotitas aytis
... tha einai: 
...            dS(t)/dt = -rho(t)*dv/dt 
... opou rho(t) i puknotita tou dialumatos ti dedomeni xroniki
... stigmi, kai dv/dt o ruthmos metavolis tou ogkou tou dialumatos.
... To prosimo "-" dilwnei tin elattwsi tis mazas tou alatiou.
... Alla rho(t) = S(t)/V opou S(t) i sunoliki maza tou alatiou
... ti xroniki stigmi t kai V o synolikos ogkos tou dialumatos o 
... opoios wstoso paramenei statheros me to xrono efoson katharos
... dialutis prostithetai me ton idio rythmo pou xanetai dialuma.
... Epomenws i diaforiki eksiswsi pou exoume na lusoume einai: 
...         dS(t)/dt = -dV/dt * S(t)/V => dS(t)/dt = -0.4 * S/20
... H theoritiki lusi tis eksiswsis aytis einai:
...  dS/S = -0.02*dt => ln(S/So) = -0.02*t => S(t) = So*exp(-0.02*t) 
... opou So i arxiki posotita tou alatiou sto dialuma (2kgr)
   ==================================================================='''   
import numpy as np
import matplotlib.pyplot as plt

def deriv(t,y):
    return Factor * y

def interpolate(x0,x1,y0,y1,yintermediate):
    if (x1-x0) != 0:
        klisi = (y1-y0)/(x1 - x0)
        if klisi != 0:
            xintermediate = x0 + (yintermediate - y1)/klisi
        else:
            xintermediate = x0
    else:
        xintermediate = x0
    return xintermediate

V_o   = 20         # lt  ogkos dialumatos
S_o   = 2.0        # kg - arxiki maza alatiou sto dialuma
S_targ = 1.0       # kg - teliki maza alatiou sto dialuma
t_fin = 8.0        # min - telikos xronos
Lrate = -0.4       # lt/min
Factor= Lrate/V_o  # /min

time = 0
dt   = 0.05        # xroniko vima
S    = S_o
S_eu = S_o
KeepLooping = True
first = True

SaltMass, SaltTheo, Time = [],[],[]
SaltMassEuler = []

while (KeepLooping):
    S_prev = S     # apothikeysi twn proigoumenwn timwn gia efarmogi tis 
    t_prev = time  # grammikis paremvolis

    S_theory = S_o * np.exp(Factor*time)  # H theoritiki lusi

    if time <= t_fin :
        Time.append(time)
        SaltMass.append(S)
        SaltTheo.append(S_theory)
        SaltMassEuler.append(S_eu)
        
    # Efarmogi tis methodo RK2
    deriv_1 = deriv(time,S)          # Derivative stin arxi tou diastimatos
    S_test = S + deriv_1 * dt        # Vima Euler sto telos tou diastimatos
    deriv_2 = deriv(time+dt, S_test) # Derivative sto telos tou diastimatos
    RK2_deriv = (deriv_1 + deriv_2)/2
    S += RK2_deriv * dt              # Vima Euler sto telos tou diastimatos
                                     # me ti mesi timi tis paragwgou

    S_eu += deriv(time,S_eu) * dt    # Methodos Euler

    time += dt

    #=================================================================
    # Eksetasi gia to an exoume fthasei sto telos twn upologismwn.
    # Gia na sumvei ayto tha prepei (a) o xronos pou exei pareltei 
    # nan einai 8min kai (b) to alati pou exei apomeinei na enai 1kgr
    #=================================================================
    if S < S_targ and first :
        t_targ = interpolate(t_prev,S_prev, time, S, S_targ)
        first = False

    if time >= t_fin and S < S_targ : KeepLooping = False

time2S_targ = np.log(S_targ/S_o)/Factor
print(50*('='))
print(' Ti xroniki stigmi t = %6.3f min'%(t_targ))
print(' H posotita alatiou sto dialuma einai: %5.2f kg'%(S_targ))
print(' Theoritika o xronos pou xreiazetai einai: %6.3f min'%(time2S_targ))
print(50*('='))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(Time,SaltMass,'bo',label='RK2')
plt.plot(Time,SaltTheo,'r-',label='Analytic')
plt.grid(True)
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel('Remaining Mass of Salt (kg)') 
#
plt.subplot(1,2,2)
plt.plot(Time,SaltMassEuler,'bo',label='Euler')
plt.plot(Time,SaltTheo,'r-',label='Analytic')
plt.grid(True)
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel('Remaining Mass of Salt (kg)') 
#
plt.tight_layout()
plt.show()
