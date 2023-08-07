#!/usr/bin/python3

import numpy as np

# Initialize empty matrix   
matrix = []   
#=========================================-=================
# Ta stoixeia mporoun na grafoun se ena file mat_input.dat
# ena noumero ana grammi kai to programma na trexei ws
# python3 lab04_prob01.py < mat_input.dat
# Tha mporoyse vevaia na dothei ws  matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]
#
# Me to np.random.randint(20,500,size=(4,4)) mporeis na pareis ena
# pinaka 4x4 me random stoixeia apo 20 ews 500
# Alla tote tha prepei na dothei a=np.random.ranint(20,500,size=(4,4))
# xwris loop
#===========================================================
'''
# Matrix input from user
nrows = int(input("Enter the number of rows: "))   
ncols = int(input("Enter the number of columns: "))   
print("Enter the entries row wise:")   
for i in range(nrows):           # A outer for loop for row entries   
   a =[]   
   for j in range(ncols):     # A inner for loop for column entries   
      a.append(np.random.randint(20,500))   
   matrix.append(a)
'''
myfile = open('listdata.dat','r')  # open the file
for line in myfile:                # read the line of the file
   a = line.split()                # Put the data of each line in the list a
   matrix.append(a)                # The data are in string format

# Print the matrix and convert the string to int (assume the numbers are integers)
print(30*'=')
print("The initial matrix ")
print(30*'=')
for i in range(len(matrix)):   
    for j in range(len(matrix[0])):
       matrix[i][j] = int(matrix[i][j])
       print("%3d"%matrix[i][j], end = " ")   
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

print(30*'=')
print("Transposed maxtrix: 1os tropos")
print("     Use of explicit loops")
print(30*'=')
for i in range(len(transposed)):   
    for j in range(len(transposed[0])):   
        print("%3d"%transposed[i][j], end = " ")   
    print()   
#====================
# 2os tropos
# list comprehension
#====================
transp = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(30*'=')
print("Transposed matrix: 2os tropos")
print("  Use of list comprehension")
print(30*'=')
# For printing the matrix   
for i in range(len(transp)):   
    for j in range(len(transp[0])):   
        print("%3d"%transp[i][j], end = " ")   
    print()   
