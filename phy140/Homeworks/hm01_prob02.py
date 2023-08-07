#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt   # Gia to erwtima (c)

'''
 (a)
'''
R = np.linspace(1,3,3)   # H entoli tha dwsei R[0]=1, R[1]=2 kai R[2]=3 ws
                         # aktines 3 diaforetikwn kyklwn
print("Oi aktines twn 3 kyklwn einai ",R)
'''
 (b)
'''
s = 2*np.pi*R            # Ypologismos tis perifereias enos kuklou. Stin
                         # prokeimeni periptwsi epeidi R einai enas array,
                         # i drasi tou pol/smou me 2*pi tha efarmostei se ola
                         # ta stoixeia tou kai to apotelesma einai enas array
print("Oi perifereies twn 3 kuklwn einai",s)

'''
 (c)
'''
plt.plot(R,s)            # i aktina einai i aneksartiti metavliti
                         # kai i perifereia i exartomeni metavliti
plt.xlabel('R(m)')
plt.ylabel('Circumference(m)')
plt.show()


