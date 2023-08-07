#!/usr/bin/python3

import numpy as np
#
def func(x):
    return 5.0 + 4.0*x - np.exp(x)
#
a = float(input("Give the low limit "))
b = float(input("Give the upper limit "))
eps = 1E-15       # epithymiti akribeia tis lusis
#
fa = func(a)
fb = func(b)
#
if fa*fb > 0:
    print('The interval does not contain the solution',fa,fb)
    exit()
#
iter = 1
while (b-a) > eps:
    c = (a+b)/2.0
    fc = func(c)
    if fc == 0:
        print('x=',c)
        exit()
    if fc * fa > 0:     # They are on the same side of the function
        a = c           # Chage of the lower limit
        fa = fc
    else:
        b = c           # They are on different sides of the functions
        fc = fc         # Change the upper limit
    iter = iter + 1
#
print('x = ',c)
print('accuracy = {:.2e}'.format(b-a))
print('f(x=',c,') = ',fc)
print(iter,' iterations needed')
