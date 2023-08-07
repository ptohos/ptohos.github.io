#!/usr/bin/python3

import numpy as np

def matprod(X,Y):
    # Initialize the resulting matrix
    N = len(X)
    M = len(X[0])
    res = [[0 for i in range(N)] for j in range(N)] 
    for i in range(len(X)):
        for j in range(len(Y[0])):    # to mikos tis grammis, diladi oi stiles 
            for k in range(len(Y)):   # to mikos tis stilis, diladi oi grammes
                res[i][j] += X[i][k]*Y[k][j]
    return res



A = [ [ 1,  3],     # O pinakas A
      [-1, -2] ] 
	    
B = [ [1, 0],       # monadiaios pinakas
      [0, 1]]

for ip in range(102):
    ipow = ip+1
    B = matprod(A,B)   # Tin prwti fora pol/zoume ton A me ton monadiaio
    
print("To apotelesma tou pinaka A^102 dinei:\n")    
for jj in range(2):
    print('[%3.0f,%3.0f]'%(B[jj][0],B[jj][1]))

