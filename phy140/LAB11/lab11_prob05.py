#!/usr/bin/python3
'''
  Programma to opoio oloklirwnei mia sunartisi pou dinetai 
  ws func1 xrisimopoiwntas tis Monte Carlo methodous oloklirwsis 
  Mesis Timis kai Deigmatolipsias. 
'''

import numpy as np
from random import seed, random

def func1(x):
    return -x**np.pi + np.pi*x

def theory(x):
    return -x**(np.pi + 1)/(np.pi + 1) + np.pi * (x*x)/2

def find_max(func,a,b):
    start_max = -1E15           # ena megalo arnitiko noumero
    ntries = 1000000            # 1M tries to find the max of the function
    for itries in range(ntries):
        xv = a + (b-a)*random()
        fxv = func(xv)
        if fxv >= start_max :
            start_max = fxv     # vrethike ena neo megisto
    return start_max

def mc_sampling(func, a, b, ntries):
    nsuccess = 0
    ymax = find_max(func,a,b)    # Eyresi tou megistou tis sunartisis
                                 # sto diastima [a,b]
    Ebox = (b - a) * ymax        # Embado tou orthogoniou pou 
                                 # perikleiei ti sunartisi
    for itries in range(ntries):
        x = a + (b-a)*random()
        y = 0 + ymax*random()
        yfunc = func(x)
        if y <= yfunc :
            nsuccess +=1
    return Ebox * nsuccess/ntries
    
def mc_mesi_timi(func,a,b,ntries):
    sum = 0.0
    for itries in range(ntries):
        xv = a + (b-a)*random()
        sum = sum + func(xv)
    return (b-a) * sum/ntries

'''
=============================================================================
 kurio programma
 Eyresi tou akrotatou tis sunartisis. Stin prokeimeni periptwsi i 
 sunartisi parousiazei akrotato sta oria oloklirwsis. Den einai 
 aparaitito na ginei kati tetoio. Mporeite na kanete to grafima tis
 sunartisis kai na vreite pou brisketai i megisti timi tis. Tha mporousate
 akoma na breite to megisto tis sunartisi vriskontas pou parousiazetai 
 i megisti timi. Tha doume sto epomeno ergastirio pws. Akoma tha mporousate
 na dialeksete mia opoiadipote timi san megisto. Sti periptwsi tis 
 askisis fmax ~ 2.1416. Tha mporousate na eixate dialeksei 2.5 i kapoia 
 alli timi pou na perikluei to max tis synartisis xwris allagi tou 
 apotelesmatos. 
 Sti periptwsi auti einai enas tropos efarmogis mia methodou pou eidate 
 gia ti lusi enos diaforetikou ymax. 
=============================================================================
''' 
lolim = float(input("Low limit of the integration: "))
uplim = float(input("Upper limit of the integration: "))
iseed = 1234567
seed(iseed)

nshots=[int(1E3),int(1E4),int(1E5),int(1E6),int(1E7),int(1E8)] # Arithmos prospatheiwn
ncases = np.size(nshots)
analytiki = theory(uplim) - theory(lolim)
labels=('Ntries','Sampling Method','MC-Theory','Mesi timi', 'MC-Theory')
print("%10s %5s %10s %10s %10s" % labels)
for ktry in range(ncases):
#    if ktry>3: break
    ntries = nshots[ktry]
    result1 = mc_sampling(func1,lolim,uplim,ntries)
    result2 = mc_mesi_timi(func1,lolim,uplim,ntries)
    print("%9d %12.6f %13.6f %10.6f %11.6f"%(ntries, result1, np.abs(result1-analytiki), result2, np.abs(result2-analytiki)))
