#!/usr/bin/python3

def suma(mxint):
    sum = 0
    for j in range(1,mxint):
        sum += j/(j+1)
    return sum

for j in range(1,4):
    mxi = 10**j
    print('For maxint %5d the sum is: %9.5f'%(mxi,suma(mxi)))

