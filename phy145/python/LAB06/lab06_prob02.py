#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

myfunc=lambda x: np.exp(-x) * np.cos(2*np.pi*x)

x1 = np.arange(0.0, 5.1, 0.1)            # Gemisma tis lista x1 kai x2 
x2 = np.arange(0.0, 5.02, 0.02)          # me times apo 0 ews 5 me vima 
                                         # 0.1 kai 0.02. Epeidi i sunartisi
                                         # arange den epistrefei tin teliki
                                         # timi (5.0) mporoume na dwsoume
                                         # ws megisti timi 5.1 kai 5.02

plt.figure(figsize=(5,7))
plt.subplot(2,1,1)
plt.plot(x1, myfunc(x1), 'bo', x2, myfunc(x2), 'g--') # Se mia entoli plot 
plt.xlim(0.,5.1)
plt.xlabel('x')
plt.ylabel(r'f(x) =  $e^{-x} cos(2\pi x)$') 
plt.subplot(2,1,2)                                    # kai ta 2 grafimata
plt.plot(x2, np.cos(2*np.pi*x2), 'r--')
plt.xlim(0.,5.1)
plt.xlabel('x')
plt.ylabel(r'f(x) = $cos(2\pi x)$')
plt.tight_layout()
plt.show()
