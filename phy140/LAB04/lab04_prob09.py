#!/usr/bin/python3

import numpy as np
#============================================================================
# Python programma gia euresi prwtwn arithmwn se kapoio diastima timwn
#
# To programma xrisimopoisei ti lista twn prwtwn diairetwn enos arithmou
# An i lista periexei ena mono stoixeio tote o aritmos einai prwtos
#==========================================================================

def factors(n):
    factorlist = []
    k = 2
    kold = 1
    while k<=n:
        while n%k == 0:
            factorlist.append(k)
            n //=k
        k +=1
    return factorlist

min_limit = int(input("Minimum value of the range:"))
max_limit = int(input("Maximum value of the range:"))
prime_list=[]
for inum in range(min_limit, max_limit+1) :
    a=factors(inum)
    nfactors = np.size(a)
    if nfactors == 1 :
        prime_list.append(inum)

nprimes = np.size(prime_list)
print("Yparxoun {:d} prwtoi arithmoi sto diastima [{:d},{:d}]. Oi ekseis:".
      format(nprimes,min_limit,max_limit))
# Ektupwsi twn arithmwn stin othoni se 15 stiles
ncol=15
for irow in range(0,int(nprimes/ncol)) :
    for icol in range(0,ncol):
        print("{:4d}".format(prime_list[(irow)*ncol+icol]),end=' ')

    print(" ")
                
