#!/usr/bin/python3

import numpy as np
import random as rng   # Library tis python gia tyxaious arithmous

def printmat(mat):
    IR = len(mat)
    try:
        IC = len(mat[0])
    except:
        IC = 0
    if IC > 0:
        for i in range(IR):   
            for j in range(IC):   
                print('%4d'%mat[i][j], end = " ")   
            print()
    else:
        for i in range(IR):
            print('%4d'%mat[i],end=" ")
        print()

print("Eisagagete ta stoixeia tis 1-D listas")
ICols = int(input("Arithmos stilwn "))
Alist = []
for IC in range(ICols):
    Alist.append(rng.randint(-20,20))
#
print("H list Alist exei stoixeia")
printmat(Alist)
#
print("Eisagagete ta stoixeia tis 2-D listas")
ICols = int(input("Arithmos grammwn "))
IRows = int(input("Arithmos stilwn "))
# Sti periptwsi ayti kanoume xrisi tis list comprehension
Blist = [ [rng.randint(-20,20) for IC in range(ICols)] for IR in range(IRows)]
print("H list Blist exei stoixeia")
printmat(Blist)
#
# Zip tis 2 listes
BzipList=list(zip(Alist, *Blist))  # To * prin to Blist dilwnei oti exoume
                                   # metavlito arithmo parametrwn sti synartisi
                                   # opws sumbainei me ton arithmo twn stilwn
print(50*"=")
print("H zipped list apotelesma twn Alist kai Blist einai")
printmat(BzipList)
