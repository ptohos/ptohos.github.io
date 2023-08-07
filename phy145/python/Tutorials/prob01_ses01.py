#!/usr/bin/python3

import numpy as np

N = int(input("Dose diastaseis nxn pinaka: "))

A = np.zeros((N,N))   # Tha mporousa na grapsw A=np.zeros([N,N])

for irow in range(N)
    A[irow, N-irow-1] = 1 

print(A)

#diaforetika:
B = np.eye(N,N)   # Pinakas B me ta stoixeia tis kurias diagwniou 1
B = B[::-1]       #<< start:stop:increment kinoumaste anapoda stis grammes
print(B)

exit()
