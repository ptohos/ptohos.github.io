#!/usr/bin/python3

import numpy as np

def printmat(mat):
    IR = len(mat)
    try:                      # Gia 2-D listes
        IC = len(mat[0])
    except:
        IC = 0                # Gia 1-D listes
    if IC > 0:
        for i in range(IR):   
            for j in range(IC):   
                print('%4.1f'%mat[i][j], end = " ")   
            print()
    else:
        for j in range(IC):   
            print('%4.1f'%mat[i][j], end = " ")   
        print()
        
IRows = int(input('Give the number of rows of the matrix '))
ICols = int(input('Give the number of coluns of the matrix '))
#==========
# zeros
#===========
zmat  = [ [float(0) for i in range(ICols)] for j in range(IRows) ]
zmat1 = np.zeros((IRows,ICols))   # Oi diastaseis dinontai ws tuple
print("====== np.zeros =====")
printmat(zmat1)
print("====== List comprehension =====")
printmat(zmat)
#==========
# ones
#===========
omat  = [ [float(1) for i in range(ICols)] for j in range(IRows) ]
omat1 = np.ones([IRows, ICols])  # Oi diastasteis dinontai ws list
print("====== np.ones =====")
printmat(omat1)
print("====== List comprehension =====")
printmat(omat)
#==============
# diagwnios 1
#===============
mres  = [ [float(1) if i==j else float(0) for i in range(ICols)] for j in range(IRows) ]
mres1 = np.eye(IRows) 
print("====== np.eye =====")
printmat(mres1)
print("====== List comprehension =====")
printmat(mres)
