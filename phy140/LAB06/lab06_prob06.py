#!/usr/bin/python3

# Initialize matrix
matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]
nrows = len(matrix)
ncols = len(matrix[0])
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
