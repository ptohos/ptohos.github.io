#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Example incorporating most of the things covered in this tutorial and previouu ones
until now.

Links:
https://www.w3schools.com/python/python_lists_comprehension.asp
'''
from myFunctions import *


# List comprehension
xList    = [i for i in range(0, 21, 1)]

# List comprehension with nested for-loop
powMin   = 0
powMax   = 4
powList  = [ [powerN(x, N) for x in xList] for N in range(powMin, powMax+1, 1) ]
if 0:
    print(powList)

# Now write to file
f = open("powers.dat", "w")

# Write the header
f.write( "{:^15s} {:^15s} {:^15s} {:^15s} {:^15s}".format("x", "powerN(x, 0)", "powerN(x, 1)", "powerN(x, 2)", "powerN(x, 3)") )
f.write("\n")
f.write( 80*"=" + "\n")

# For-loop: All lists of int
for v,w,x,y,z in zip(xList, powList[0], powList[1], powList[2], powList[3]):
    line =  "{:^15d} {:^15d} {:^15d} {:^15d} {:^15d}".format(v, w, x, y, z)
    f.write(line + "\n")
f.write( 80*"=" + "\n")
f.close()


# Now read the file
f = open("powers.dat", "r")
lineList = f.read().split("\n")
for l in lineList:
    print(l)

quit()
