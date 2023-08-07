#!/usr/bin/python3
'''
------------------------------------------------------------
 Monte Carlo gia proseggisi tis pithanotitas na paroume 
 sugkekrimeno arithmo kata ti ripsi enos zariou: (i.e. 6)

 H pithanotita einai 1/6 afou to zari exei 6 noumera kai 
 epomenws i pithanotita na paroume opoiodipote noumero apo 1-6
 einai akrivws idia gia ola ta noumera

 Epomenws i theoretiki pithanotita einai 1/6

 Gia na lusoume to problima tha metatrepsoume tous tyxaious 
 arithmous kai anti na pernoun times sto diastima [0,1] tha 
 pairnoun akeraies tyxaies times apo 1 ews 6 afou ayta einai
 ta noumera pou mporoume na exoyme

 Tha xrisimopoiisoume ti Methodo Monte Carlo gia difforetiko
 plithos prospatheiwn.
------------------------------------------------------------
'''
import numpy as np
from random import random, seed, randrange
iseed = 123456
desiredside = 6               #timi poy theloume
seed(iseed)

for iexp in range(1,7):  # Tha dokimasoume ews 10^7 prospatheies
    ntries = 10**iexp    # plithos prospatheiwn 
    nsuccess = 0         # metritis gia kathe periptwsi epituxias

    for itries in range(ntries):
        side = randrange(1,7)  # Etsi tha paroume tyxaies 
                               # akeraies times apo 1 ews 6
        if side == desiredside:  nsuccess +=1
    if iexp == 1:
        print("\n Prospathies     Pithanotita") 
    print(" %7d %16.4f" % (ntries,nsuccess/ntries))
