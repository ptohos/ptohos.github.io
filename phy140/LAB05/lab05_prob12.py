#!/usr/bin/python3

import numpy as np

inpfile=input('Give the name of the file ')
file2read = open(inpfile,'r')
mxlen=30
A=[]
for i in range(mxlen+1):
    A += [0]

for lines in file2read:
    try:
        numb = int(lines.strip())
    except:
        continue
    A[numb] += 1          # Ayksanoume ti thesi numb tou pinaka A 

file2read.close()
print('Arithmos Suxnotita')
for jj in range(1,len(A)):
    print(" %3d %8d"%(jj,A[jj]))

tota = sum(A)
print("Sum of the numbers is ",tota)
