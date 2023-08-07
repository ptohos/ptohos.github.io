#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
More on functions and their use

Links:
https://www.w3schools.com/python/python_functions.asp
'''
from myFunctions import *

# Can get help for the usuage of a function (provided the user has added it!!)
if 0:
    help(powerN) # this is interactive so avoid using inside a script

helpForPowerN=powerN.__doc__
print("The docstrings of custom function powerN() are shown below: %s" % (helpForPowerN) )


# Understand that function parameters use variables by reference (same memory location)
numList = [1, 3, 5, 7, 9]
print("\n=== Printing numList before calling increment()")
print("\t%s" % (numList) )

print("=== Printing numList after calling increment()")
increment(numList)
print("\t%s" % (numList) )


# Looping simultaneously over 2 lists
evenList = [z for z in range(10) if z%2==0]
oddList  = [z for z in range(10) if z%2!=0]
print("=== Using zip() to loop over 2 lists simultaneously:")
for odd,even in zip(oddList, evenList):
    print("\todd=%d, even=%d" % (odd, even) )


# Summing over a list with sum()
oneList  = [1 for i in range(5)]
print("oneList=%s, sum(oneList)=%d" % (oneList, sum(oneList)) )
    
print("\n=== Quit!")
quit()

