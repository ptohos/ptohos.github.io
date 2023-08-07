#!/usr/bin/python3

import numpy as np
import matplotlib as plot


a=float(input("Dose timi gia ton oro a "))
b=float(input("Dose timi gia ton oro b "))
c=float(input("Dose time gia ton oro c "))
diakrinousa = b*b - 4 * a * c
if diakrinousa >= 0:
    pass
else:
    a = a + 0j
    b = b + 0j
    c = c + 0j
    diakrinousa = b*b - 4 * a * c

x1=(-b + np.sqrt(diakrinousa)) / (2*a) 
x2=(-b - np.sqrt(diakrinousa)) / (2*a)
print(x1,x2)
quit()

