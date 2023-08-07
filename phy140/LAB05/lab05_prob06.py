#!/usr/bin/python3

import numpy as np

# Matrix input from user
nrows = int(input("Enter the number of rows: "))   
ncols = int(input("Enter the number of columns: "))   
# Initialize empty matrix   
matrix = []   
print("Enter the entries row wise:")   
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
for i in range(nrows):        # A outer for loop for row entries   
   a =[]   
   for j in range(ncols):     # A inner for loop for column entries   
      a.append(np.random.randint(20,500))   
   matrix.append(a)
'''
inpfile = open("listdata.dat",'r')
for line in inpfile:
   a = line.split()
   matrix.append(a)

# Print the matrix   
for i in range(len(matrix)):      #posa stoixeia lists exei (ara poses grammes)
    for j in range(len(matrix[0])):  #posa stoixeia exei to 0th list-stoixeio
                                     #epomenws poses stiles
       matrix[i][j] = int(matrix[i][j])
       print(matrix[i][j], end = " ")   
    print()   

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
