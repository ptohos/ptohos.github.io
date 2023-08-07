#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to importing custom functions

Links:
https://python.land/introduction-to-python/functions
'''
from myFunctions import *

say_hi()

# Get string input from user
num, exp = getTwoInts()
try:
    numExp = powerN( num, exp)
    print("=== powerN(%d, %d) = %d" % (num, exp, numExp) )
except:
    print("=== Something went wrong!")
        
# Can repear procedure as many times as we like
print("\n=== Another example")
num, exp = getTwoInts("Please insert value (int) for x: ", "Please insert value (int) for exponent: ", )
print("=== powerN(%d, %d) = %d" % (num, exp, powerN( num, exp)) )


print("=== Quit!")
quit()
