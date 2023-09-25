#!/usr/bin/python3

import numpy as np

A=[0,0,0,0,0,0,0,0,0,0]
A[5] = 11


A = np.zeros(10,dtype=int) # Dimiourgia enos numpy array me arxikes times 0
                           # kai times akeraious. Default einai real
A[5] = 11                  # Anathesi tis timis 11 sto 6 stoixeio tou array
                           # ksekinontas tin arithmisi apo to 0
print(A)

'''
  Tha mporousame na xrisimopoiisoume list kai ena loop
'''
A = []              # Dimiourgia mias adeias listas
for j in range(10): # 
    A +=[0]         # Prosthetoume sti lista mia lista me stoixeio [0]
                    # Ayto einai idio me to na grapsoume A.append(0)
    if (j==5): A[j] = 11

print(A)

'''
  Tha mporousame na xrisimopoiisoume list comprehension
'''
A = [0 if j != 5 else 11 for j in range(10)]
print(A)


quit()
