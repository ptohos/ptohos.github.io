#!/usr/bin/python3

import numpy as np

x = []
y = []
for num in range(10,51,5):
    x += [num]             # Fill in the number in th ex list
    y += [2*num-15]        # and in the y list
    
outfile="lab06_prob01.dat"
file_handle = open(outfile,"w")
for i in range(len(x)) :
    file_handle.write( "%5d %5d\n"%(x[i],y[i]) )
file_handle.close()
