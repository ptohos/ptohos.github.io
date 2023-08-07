#!/usr/bin/python3

import numpy as np

nrows = int(input("Number of rows? "))
ncols = int(input("Number of columns? "))
B  = [0]*ncols       # monodiastati list me arithmo stoixeiwn oses oi stiles
                     # kai timi 0
C  = [1]*ncols       # monodiastati list me arithmo stoixeiwn oses oi stiles
                     # kai timi 1
A  = [B]*nrows       # orismos list me arithmo stoixeiwn iswn me tis grammes
                     # kai times kathe stoixeioy ti lista B. Epomenws exoume
                     # mia lista me stoixeia listes
print("Arxiki morfi me ola ta stoixeia 0")
print(A)             # A list with 0 pantou
#
A[0][0]=1            # Antikatastasi twn stoixeiwn tis 1-stilis me 1 
print("Allagi me ola ta stoixeia tis 1i-s stilis 1")
print(A)
#
A[0][ncols-1]=1      # Antikatastasi twn stoixeiwn tis teleutaias stilis me 1
print("Allagi me ola ta stoixeia tis %di-s stilis 1"%ncols)
print(A)
#
A[0] = C             # Antikatastasi tou 1ou stoixeiou tis list A
                     # (pou einai list) me mia alli list ta stoixeia tis einai 1
print("Allagi me ola ta stoixeia tis 1i-s grammis 1")
print(A)
A[nrows-1] = C       # Antikatastasi toy teleutaioy stoixeiou tis list A
                     # tis teleytaias grammis tou A diladi, me ti list C
print("Allagi me ola ta stoixeia tis %di-s grammis 1"%nrows)
print(A)

'''
Xrisimopoiontas numpy arrays
A=np.zeros((nrows,ncols),dtype=int)  # dimiourgia enos array A nrows x ncols

print(A)


A[::nrows-1,::]=1       #Antikatastasi me tin timi 1 gia ola ta stoixeia tou
                        #array A ksekinontas apo tin 0-grammi ews tin n-grammi
                        #me vima nrows-1, gia ola tis stiles kathe grammis

A[::,::ncols-1]=1       #Antikatastasi me tin timi 1 gia ola ta stoixeia tou
                        #array A ksekinontas apo tin stili 0 ews tin teleutaia
                        #stili kinoumenoi me vima ncols-1. Diladi mono tin
                        #stili 0 kai 0+ncols-1 pou einai se arithimisi i
                        #teleytaia stili, gia oles ta stoixeia kathe stilis
                        #diladi tis grammes ::
print(A)
'''
