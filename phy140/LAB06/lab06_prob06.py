#!/usr/bin/python3

import numpy as np
mxCount = int(input('How many numbers to search for [2]:'))
n = 0
step = 14
divisibleBy7 = False
perfectSqr = False
count = 0
NumbersFound = []
while (not(divisibleBy7 and perfectSqr) and count < mxCount):
    n = n + step
    if n%7 == 0:
        divisibleBy7 = True
    IsSqrt = int(np.sqrt(float(n)))
    if IsSqrt*IsSqrt - n == 0:
        perfectSqr = True
    if (perfectSqr and divisibleBy7):
        count = count + 1
        NumbersFound.append(n)
        divisibleBy7 = False
        perfectSqr = False

print('\nOi prwtoi %d artioi diairoumenoi me 7 pou einai teleia tetragwna einai:'%mxCount)
for i in range(mxCount):
    print('%2d) einai: %6d'%(i,NumbersFound[i]))

quit()
