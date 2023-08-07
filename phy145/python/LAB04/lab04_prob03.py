#!/usr/bin/python3

#==========================================
# Sto provlima ayto o arithmos twn stilwn
# gia kathe grammi den einai statheros
# alla allazei
#=======================
import numpy as np

A = [ [3,3], [4,2,9], [8,3,5,1], [7,6] ]

totsize = 0
for rows in A:
    IC = len(rows)
    totsize += IC
print("The size of the A matrix is : ",totsize)

