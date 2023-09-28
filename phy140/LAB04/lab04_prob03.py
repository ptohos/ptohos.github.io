#!/usr/bin/python3

import numpy as np
#============================================================================
# Python programma to opoio vriskei tous diairetes enos arithmou
# poy einai prwtoi arithmoi.
# Ayto to kanoume mesw mias synartisis pou dexetai ws orisma enan
# arithmo tou opoiou theloume tous prwtous diairetes.
# Orizetai mia lista i opoia arxika einai adeia kai stin opoia
# apothikeuontai oi diairetes. Oi diairetes vriskontai diairontas
# arxika ton arithmo me ton prwto prwto diaireti. To piliko tis
# diairesis diaireitai kai pali me ton idio prwto kai i diadikasia
# sunexizetai ews otou to upoloipo einai diaforetiko apo 0.
# O diairetis allazei kai lambanetai o amesws epomenos kai i diadikasia
# sunexizei me to enapomeinonta arithmo.
# Gia paradeigma estw o arithmos 24
# arxika k =2 opote:
#     1 epanalipsi 24/2 = 12
#     2 epanalipsi 12/2 =  6
#     3 epanalipsi  6/2 =  3
#     4 epanalipsi  3/2 =  1 to upoloipo einai diaforetiko tou 0
#     Epomenws i factorlist tha periexei 2,2,2
# To n einai twra 3
#  kai profanws diaireitai me k=3 ;opvw ginetai o diaireteis
# H sunartisi epistr;efe ti lista me tou diairetes
# An i lista exei mono 2 stoixeia to 1 kai to num tote o num einai prwtos.
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

num = int(input("Give a number: "))
a=factors(num)
nfactors = np.size(a)
print("Oi prwtoi diairetes tou arithmou {:d} einai: ".format(num))

for numb in a:
    print("{:d}".format(numb), end=' ')
if nfactors == 1:
    print("O arithmos einai prwtos")

print(" ")





