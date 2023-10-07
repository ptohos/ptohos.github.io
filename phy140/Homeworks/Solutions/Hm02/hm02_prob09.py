#!/usr/bin/python3

import numpy as np

J = int(input("Dose ton 1o arithmo: "))
K = int(input("Dose ton 1o arithmo: "))

res = [J,K]

for i in range(48): #upologizei ta epomena 48 noumera
    res.append[res[i]+res[i+1]]

my_file = open("fibonacci.dat","w")
for i in range(0,46,5):
    my_file.write("%d   %d   %d   %d   %d\n"%(res[i],res[i+1],res[i+2],res[i+3],res[i+4]))
my_file.close()

exit()
