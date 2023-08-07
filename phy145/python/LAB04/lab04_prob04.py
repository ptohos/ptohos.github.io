#!/usr/bin/python3

import numpy as np

# Matrix input from user
row = int(input("Enter the number of rows:"))   
column = int(input("Enter the number of columns:"))   
# Initialize empty matrix   
matrix = []   
print("Enter the entries row wise:")   
#=========================================-=================
# Ta stoixeia mporoun na grafoun se ena file mat_input.dat
# ena noumero ana grammi kai to programma na trexei ws
# python3 lab04_prob01.py < mat_input.dat
#===========================================================
for i in range(row):           # A outer for loop for row entries   
   a =[]   
   for j in range(column):     # A inner for loop for column entries   
      a.append(int(input()))   
   matrix.append(a)
# Tha mporoyse vevaia na dothei ws  matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]
# Print the matrix   
for i in range(len(matrix)):   
    for j in range(len(matrix[0])):   
        print(matrix[i][j], end = " ")   
    print()   
#====================
# 1os tropos
# 2 explicit loops
#===================
transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(20*'=')
print("1os tropos")
for i in range(len(transposed)):   
    for j in range(len(transposed[0])):   
        print(transposed[i][j], end = " ")   
    print()   
#====================
# 2os tropos
# list comprehension
#====================
transp = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(20*'=')
print("2os tropos")
# For printing the matrix   
for i in range(len(transp)):   
    for j in range(len(transp[0])):   
        print(transp[i][j], end = " ")   
    print()   
#=====================
# 3os tropos
# np methodos transpose()
#=====================
matrix = np.array(matrix)
TheTransp = matrix.transpose()
print(20*'=')
print("3os tropos")
# For printing the matrix   
for i in range(len(TheTransp)):   
    for j in range(len(TheTransp[0])):   
        print(TheTransp[i][j], end = " ")   
    print()   
#==================
# 4os trops
# np sunartisi T
#==================
mat=matrix.T
print(20*'=')
print("4os tropos")
for i in range(len(mat)):   
    for j in range(len(mat[0])):   
        print(mat[i][j], end = " ")   
    print()   
