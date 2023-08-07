#!/usr/bin/python3

import numpy as np
import matplotlib as plot

a = 2 + np.exp(2.8) /( np.sqrt(13) - 2 )
b = ( 1 - ( 1 + np.log(2))**(-3.5) ) / ( 1 + np.sqrt(5) )
c = np.sin( ( 2 - np.sqrt(2) ) / ( 2 + np.sqrt(2) ) )  # Prosoxi to orisma
                                                       # twn trigonommetrikwn
                                                       # synartisewn einai
                                                       # se rad oxi moires

print(" a = %8.4f b = %8.4f c = %8.4f"%(a,b,c))

