#!/usr/root/python3

import numpy as np

def fillmatrix(X):
    A=[]
    for jj in range(len(X)):
        yval = X[jj]*X[jj] + 2*X[jj] + 1
        A +=[yval]
    return np.array(A)                    # Epistrofi enos np array

Xinp = np.arange(-20,21,1)
print('To mikos tou pinaka einai: ',len(Xinp))
Yinp = fillmatrix(Xinp)
#
fileout = open('lab03_prob08.out','w')    # Anoigma enos file gia eggrafi
for jj in range(len(Xinp)):
    fileout.write('%3d %6d'%(Xinp[jj],Yinp[jj]))
fileout.close()


#====2os tropos - mono me np arrays
XXinp = np.arange(-20,21,1)
YYinp = XXinp**2 + 2*XXinp +1
np.savetxt("lab03_prob08_np.out",list(zip(XXinp,YYinp)),fmt='%3d %6d')

'''
Sunithws savetxt xrisimopoieitai gia 1-D or 2-D arrays. Wstoso, 
stin pio panw entoli savetxt, xrisimopoiithike ena neo antikeimeno 
ayto pou dinetai apo to zip. To apotelesma tou zip einai na parei 
mia seira apo lists kai na dimiourgisei ena antikeimeno tou opoiou 
kathe thesi i apoteleitai apo ta stoixeia sti thesi i tis kathe listas.  
Epomenws an exoume gia paradeigma 2 listes A=[A1,A2,A3,A4] kai mia 
lista B=[B1,B2,B3,B4,B5]  to antikeimeno zip(A,B) utha exei stoixeia
([A1,B1],[A2,B2], [A3,B3], [A4,B4]). Opws paratireitai to neo antikeimeno
mporei na enwsei tis dyo listes se mikos oso to mikos tis mikroteris. 
To zip antikeimeno metatrepetai se list me ti methodo list. Epomones 
metatrepoume to antikeimeno se 2-D lis
'''
