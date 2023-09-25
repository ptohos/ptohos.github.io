#!/usr/bin/python3

import numpy as np

A=np.random.randint(0,100,size=20)  # Dimiourgia enos 1-D array megethous 20
                                    # me tyxaies int times sto diastima 0 - 100
A=[1,2,3,4,5,6,7,8,9,10]
print(A)
B=A[-1::-1]  # Ksekinoume apo to stoixeio tou array perissotero deksia [-1]
               # kai kinoumaste pros to stoixeio perissotero aristera 
               # me arnitiko vima [-1]. Prosoxi oti an bazame ws teleutaio
               # stoixei to 0 (diladi A[-1:0:-1] tote to A[0] den tha tupwnontan
               # giati to diastima sto slicing einai anoikto)
               # Epeidi to vima einai arnitiko tha
               # mporousame na grapsoume apla A[::-1]
print(B)
'''
Tha mporousame na grapsoume apla  print(A[::-1]) xwris na kratisoume tin
anastremeni lista
'''
