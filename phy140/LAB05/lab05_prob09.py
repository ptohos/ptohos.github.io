#!/usr/bin/python3

import numpy as np

floatNumbers = []

n = int(input("Enter the list size : "))

print("\n")
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers +=[item]
    
for i in range(len(floatNumbers)):
    print("%8.3f"%(floatNumbers[i]))
