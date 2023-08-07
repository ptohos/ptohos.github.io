#!/usr/bin/python3

import numpy as np

def factorial(n):
    fact = 1.
    for i in range(n,0,-1):
        fact=fact*i
    return fact

def poisson(fact,Ave,Nobs):
    if Nobs > 0:
        fact=fact(Nobs)
    else:
        fact=1
        print("Factorial of zero or negative number")
        return -1
    return Ave**Nobs * np.exp(-Ave)/fact


ave=int(input("Give the average number of events "))
NMax=int(input("Give the maximum number of observed events "))

print(60*'=')
print("Poisson probability to observe events when %d is the mean" % ave)
print(60*'=')
print("%24s %14s"%("Nobserved","Probability"))
suma=0
for ievents in range(1,NMax+1):
    poisprob = poisson(factorial,ave,ievents)
    print('{:20d} {:15.4f}%'.format(ievents,poisprob*100))
    suma +=poisprob
print(60*'=')
print('suma = {:7.4f}%'.format(suma*100))
