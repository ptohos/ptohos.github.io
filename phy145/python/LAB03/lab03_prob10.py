#!/usr/bin/python3

import numpy as np
import random as rng     # Xrisi tou module random gia na gemisoume to pinaka A
                         # me tuxaious arithmous

def symmetric(X):
    isSymmetric = False
    suma  = 0
    nrows = len(X)
    ncols = len(X[0])
    if nrows != ncols :
        print('The given matrix can not be symmetric')
        print('because it is not orthogonal')
        return isSymmetric
    # Gia na exetasoume an o pinakas einai symmetrikos tha prepei na
    # eksetasoume ta simeia panw apo tin kuria diagwnio kai na ta
    # sugkrinoume me ayta katw apo tin kuria  diagonio
    for iR in range(nrows-1):
        for iC in range(iR,ncols):
            suma = suma + np.abs(X[iR][iC] - X[iC][iR])  # An to athroisma einai
    if suma == 0:  isSymmetric = True                    # 0 einai symmetrikos
    return isSymmetric


def transp(X):
    #==============================
    # O anastrofos tha exei arithmo grammwn oso o aritmos stilwn tou arxikou
    # kai arithmo stilwn oso o arithmos grammwn tou arxikou. Diladi
    # an o arxikos pinakas einai [IR,IC] o anastrofos tha einai [IC,IR]
    #==============================
    nrows = len(X)
    ncols = len(X[0])
    # Dimiourgia tou anastrofou
    Tmat = [[0 for iC in range(nrows)] for iR in range(ncols)]
    #
    for iR in range(nrows):
        for iC in range(ncols):
            Tmat[iC][iR] = X[iR][iC]
    return Tmat


MRows = int(input('Give the number of rows [MRows] of the matrix '))
NCols = int(input('Give the number of columns [NCols] of the matrix '))
#===== Define the matrix in python ===========
A = [[0 for iC in range(NCols)] for iR in range(MRows)]

for iR in range(MRows):
    for iC in range(NCols):
        A[iR][iC] = rng.randint(0,20)   # epistrefei enan random integer sto 
                                        # diastima [0,20] (kleisto diastima]
print(" O pinakas A einai:")
for rows in A:
    print(rows)
B = transp(A)
print("O anastrofos pinakas tou A einai:")
for row in B:
    print (row)
if symmetric(A):
    print(" O pinakas A einai symmetrikos ")
else:
    print(" O pinakas A den einai summetrikos")

        
