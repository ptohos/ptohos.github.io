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


'''
Gia megalous arithmous yparxei kindunos yperxeilisis toso
apo ton upologismo toy paragontikou oso kai apo ton ypologismo
twn ekthetikwn. Gia to logo ayto mporoume na periorisoume ta
terastia noumera xrisimopoiontas ton logarithmo tis sxesis:
P = [e^(-m) * m**n]/n! => log(P) = log(e^(-m)) + log(m**n) - log(n!)
=> log(P) = -m + n*log(m) - Sum_i=1^n (log(i))
O logarithmos toy paragontikou einai to athroisma twn logarithmwn twn
arithmwn.
Ara to ginomeno ginetai athroisma peperasmenwn arithmwn.
Ypologizoyme to log(P) kai katopin tin poisson pithanotita
apo ti sxesi P = e^log(P)
'''
def logfactorial(n):
    logsum = 0
    if (n >=0):
        for i in range(1,n+1):
            logsum += np.log(i)
    else:
        print("Undefined factorial")
        logsum = -1
    return logsum

Nevts = [0,1E6]
Nevts = [int(x) for x in Nevts]   # convert the list elements to integers
Means = [10,1E6]
Means = [int(x) for x in Means] 
for i in range(len(Nevts)) :
    logP = -Means[i] + Nevts[i] * np.log(Means[i]) - logfactorial(Nevts[i])
    PoisProb = np.exp(logP)
    print(60*'=')
    print("Poisson probability to observe %6d events with mean of %6d is %.2f%%" %(Nevts[i],Means[i],PoisProb*100))
    print(60*'=')


