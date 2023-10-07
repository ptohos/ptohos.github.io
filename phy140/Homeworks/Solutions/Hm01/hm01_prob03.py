#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt   # Gia to erwtima (c)

'''
 (a)
'''
L = np.linspace(1,3,3)   # H entoli tha dwsei L[0]=1, L[1]=2 kai L[2]=3 ws
                         # pleyres 3 diaforetikwn kubwn
print("Oi pleures twn 3 kubwn einai",L)
'''
 (b)
'''
V = L**3                 # Ypologismos tou ogkou tou kubou. Stin prokeimeni
                         # periptwsi epeidi L einai enas array, i drasi tou
                         # ekthetikou tha efarmostei se ola ta stoixeia tou
                         # kai to apotelesma tha einai enas array
print("Oi ogkoi twn 3 kubwn einai",V)

'''
 (c)
'''
plt.plot(L,V)            # i pleura einai i aneksartiti metavliti kai o ogkos
                         # i exartomeni metavliti
plt.xlabel('L(m)')
plt.ylabel('Volume(m$^3$)')
plt.show()


