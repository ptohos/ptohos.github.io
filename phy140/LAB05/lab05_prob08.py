#!/usr/bin/python3

import numpy as np

x = []
y = []
for num in range(10,51,5):
    x += [num]             # Fill in the number in th ex list
    y += [2*num-15]        # and in the y list
    
for i in range(len(x)) :
    print( "%3d %6d"%(x[i],y[i]) )

