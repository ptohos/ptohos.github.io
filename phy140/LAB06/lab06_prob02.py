#!/usr/bin/python3

import numpy as np

floatNumbers = []

n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)
    
outfile="lab06_prob02.dat"
file2write = open(outfile,"w")
for i in range(len(floatNumbers)):
    file2write.write("%8.3f\n"%(floatNumbers[i]))
file2write.close()
