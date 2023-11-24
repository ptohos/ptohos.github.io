#!/usr/bin/python3
'''
  Programma to opoio oloklirwnei mia sunartisi pou dinetai 
  ws func1 xrisimopoiwntas tis Monte Carlo methodous oloklirwsis 
  Mesis Timis kai Deigmatolipsias. 
  To programma episis efarmozei ti methodo Newton gia tin 
  euresi tou megistou tis sunartisis pros oloklirwsi. 
  To akrotato brisketai zitontas i paragwgos na midenizetai 
'''

import numpy as np
from random import seed, random

def func1(x):
    return -x**np.pi + np.pi*x

#... H 1-i paragwgos tis sunartisis func1
def d1x(x):
    return -np.pi*x**(np.pi-1) + np.pi

#... H 2-i paragwgos tis sunartisis func2
def d2x(x):
    return -(np.pi)*(np.pi-1)*x**(np.pi-2)    

def theory(x):
    return -x**(np.pi + 1)/(np.pi + 1) + np.pi * (x*x)/2

def find_max_newton(x0,f,df,eps,istepmx):
    '''
    ==========================================================
        Inpug arguments: x0     arxiki pithani lusi
                         f      i sunartisi 
                         df     i 1-i paragwgos
                         eps    i epithumiti akriveia tis lusis
                         istepm  megistos arithmos vimatwn
    ==========================================================
    '''
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error    # The new solution 
        x0 = x1            # The new solution becomes the old solution for the
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1
            break
#
    return x0,flag,istep

def find_max_mc(func,a,b):
    start_max = -1E15           # ena megalo arnitiko noumero
    ntries = 1000000            # 1M tries to find the max of the function
    for itries in range(ntries):
        xv = a + (b-a)*random()
        fxv = func(xv)
        if fxv >= start_max :
            start_max = fxv     # vrethike ena neo megisto
    return start_max

def mc_sampling(func, ymax, a, b, ntries):
    nsuccess = 0
    Ebox  = (b - a) * ymax         # Embado tou orthogoniou pou 
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
 i megisti timi. Akoma tha mporousate na dialeksete mia opoiadipote timi 
 san megisto. Sti periptwsi tis askisis fmax ~ 2.1416. Tha mporousate na 
 eixate dialeksei 2.5 i kapoia alli timi pou na perikluei to max tis 
 synartisis xwris allagi tou apotelesmatos.
 Stin askisi ayti ginetai toso me ti methodo Newton oso kai me tin 
 methodo mc  
=============================================================================
''' 
lolim = float(input("Low limit of the integration: "))
uplim = float(input("Upper limit of the integration: "))
iseed = 1234567
seed(iseed)

#... Mia lista me ton arithmo twn prospatheiwn
nshots=[int(1E3),int(1E4),int(1E5),int(1E6),int(1E7),int(1E8)]
ncases = np.size(nshots)

#... H analutiki lusi tou oloklirwmatos
analytiki = theory(uplim) - theory(lolim)

#... Eyresi tou megistou tis sunartisis
fmax1 = find_max_mc(func1,lolim,uplim) # Eyresi tou megistou me MC
#... Euresi megistou me ti methodo MC
mx_guess = 2.
epsi = 1e-15
mxit = 20
dmax2,flag,istep = find_max_newton(mx_guess,d1x,d2x,epsi,mxit)
if flag != 0:
    print("Den vrethike akrotato me ti methodo MC")
    fmax2 = 1E9
else:
    fmax2 = func1(dmax2)      # dmax2 einai to x pou midenizei tin paragwgo

print('MC-megisto: ',fmax1, ' Megisto ala Newton: ', fmax2)
fmax = fmax2   # H methodos Newton einai perissotero akribis apo tou MC


#...
labels=('Ntries','Sampling Method','MC-Theory','Mesi timi', 'MC-Theory')
print("%10s %5s %10s %10s %10s" % labels)
#...
for ktry in range(ncases):
    ntries = nshots[ktry]
    result1 = mc_sampling(func1,fmax,lolim,uplim,ntries)
    result2 = mc_mesi_timi(func1,lolim,uplim,ntries)
    print("%9d %12.6f %13.6f %10.6f %11.6f"%
          (ntries, result1,np.abs(result1-analytiki),
           result2, np.abs(result2-analytiki) ))
