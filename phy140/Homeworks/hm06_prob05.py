#!/usr/bin/python3

from sympy import *

x = Symbol('x')
f = (x**(4/5)) * ((x-4)**2)   
first_deriv  = diff(f)                   #first derivative
second_deriv = diff(first_deriv)         #second derivative
print("f' =", first_deriv)

print("Critical Values are:")

# Solve on first_deriv 
dRoots = solve(first_deriv)              #returns a list
print(dRoots, '\n')
for root in dRoots:
    second_deriv_val = second_deriv.subs(x, root)
    print(f"At root {root:7.5f}, second derivative at this point is {second_deriv_val:7.5f} which is f{'less' if second_deriv_val < 0 else 'greater'} \
    than zero, so this is a local {'minimum' if second_deriv_val < 0 else 'maximum'}")
