#!/usr/bin/python3

import sympy as sp

x = sp.Symbol('x')

a = sp.integrate(sp.exp(-x))
print("To oloklirwma tis exp(-x) = ",a)

res=sp.integrate(sp.exp(-x),(x,0,'oo'))
print("To oloklirwma tis exp(-x) sto diastima [0,oo] einai: ",res)

quit()
