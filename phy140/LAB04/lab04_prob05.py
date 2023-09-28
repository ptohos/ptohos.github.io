#!/usr/bin/python3

import numpy as np
import matplotlib as plot

def sinc(x) :
    if x == 0.0 :
        y = 1.0
    else :
        y = np.sin(x)/x
    return y

x = np.arange(-5.,5.5,0.5)   # Perilamvanoume to +5
xy = np.linspace(-5.,5.,21) # Tha mporousame na exoume auti ti sunartisi
                            # To euros einai 10 monades (5-(-5)=10) kai
                            # exoume 20 upodiastimata wste to euros na einai
                            # 10/20 = 0.5 kai prosthetoume 1 akoma gia na
                            # xrisimopoiisoume panta tis duo akraies times
for xx in x:
    if (xx>=0) :
        print("  %5.3f %10.3f" % (xx,sinc(xx) ) )
    else : 
        print(" %4.3f %10.3f" % (xx,sinc(xx) ) )
        
print("\n Using the array defined with linspace function\n")
for xx in xy:
    if (xx>=0) :
        print("  %5.3f %10.3f" % (xx,sinc(xx) ) )
    else : 
        print(" %4.3f %10.3f" % (xx,sinc(xx) ) )

        
