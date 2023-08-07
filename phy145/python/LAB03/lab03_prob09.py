#!/usr/bin/python3

def ycalc(x):
    return x**2 -x

for xv in range(4):
    yv = ycalc(float(xv))
    print('%3.1f %5.1f'%(xv,yv))

    
