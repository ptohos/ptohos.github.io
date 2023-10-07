#!/usr/bin/python3

import numpy as np

xval = float(input("Give a number to estimate its logarithm "))
lowVal,hiVal = input("Lower and Upper limit of the number of terms ").split()
tstep = int(input("Step size to vary the number of terms in the series "))
lowVal = int(lowVal)
hiVal = int(hiVal)

for N in range(lowVal,hiVal+tstep,tstep):  # Different cases for number of terms
    SerieSum=0                             # For each option initialize the sum
    for i in range(1,N+1):                 # The series for the option of N
        SerieSum += ((-1)**(i+1))*((xval-1)**i)/i
    
    if N == lowVal :                       # Head line - print it once 
        print(" Nterms      Series Sum     ln(%.4f)" % xval)
    print("{:5d} {:18.10f} {:14.10f}".format(N,SerieSum,np.log(xval)))

exit()
