#!/usr/bin/python3

import numpy as np

low_limit=float(input('Dwste to katwtero orio [rads] '))
up_limit=float(input('Dwste to anwtero orio [pol/sio tou pi] '))
frac=float(input('Dwste to klasma tou pi gia tin allagi gwnias '))
print()
twopi    = 2.*np.pi
up_limit = up_limit * np.pi
step     = np.pi/frac
'''==========================================
 Ta akoloutha einai paradeigma tis xrisis
 tis entolis format gia na grapsoume to 
 trigwnometriko pinaka stoixismeno
=========================================='''
angle = low_limit
i = 0
while angle <= up_limit :
    i = i + 1
    if i == 1 : 
        print(2*'',11*'=',' Trigonometric List', 11*'=')
        print('%7s %12s %10s'%('x','sin(x)','cos(x)'))
    print(' {0:9.6f}  {1:9.6f}  {2:9.6f}'.format(angle, np.sin(angle), np.cos(angle)))
    angle = angle + step

quit()
