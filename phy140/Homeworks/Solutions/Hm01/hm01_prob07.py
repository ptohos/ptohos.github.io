#!/usr/bin/python3

from numpy import abs

def f(x):
    return x

def g(x):
    return x**2

N = int(input("Give the number of check points N: "))
epsilon = float(input("Give the error tolerance: "))

x_values=[]
xmax = 4
xmin = -4
dx = (xmax - xmin)/N
x = xmin
while x <= 4:
    x_values +=[x]
    x +=dx

# Check if the difference between the function values for each x
# is smaller than the allowed tolerance

for x in x_values:
    if abs(f(x) - g(x)) < epsilon :
        print("Intercept points : ", x)
'''
Yparxoun 2 luseis oi opoies den einai akribws 0 kai 1
Auto eksartatai apo to N pou dialegoume. Mporei na broume
2, 1 akoma kai kamia. En genei an to epsilon paramenei
stathero tote auksanontas to N mporei se mia perioxi na
broume polles luseis.
'''

