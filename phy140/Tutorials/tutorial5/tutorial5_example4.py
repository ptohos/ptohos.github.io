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
https://www.nobelprize.org/prizes/physics/1933/dirac/biographical/
'''
from myFunctions import say_hi
from myFunctions import getList
from myFunctions import sumList
from myFunctions import prodList

say_hi("Paul Dirac", 3, 5, "PHYS-140")

# Get list from user
myNums = getList()

print("=== List sum: %d" % (sumList(myNums) ) )
print("=== List product: %d" % (prodList(myNums) ) ) 
# try:
#     numExp = f.powerN( num, exp)
#     print("=== powerN(%d, %d) = %d" % (num, exp, numExp) )
# except:
#     print("=== Something went wrong!")
#         
# # Can repear procedure as many times as we like
# print("\n=== Another example")
# num, exp = f.getTwoInts("Please insert value (int) for x: ", "Please insert value (int) for exponent: ", )
# print("=== powerN(%d, %d) = %d" % (num, exp, f.powerN( num, exp)) )


print("=== Quit!")
quit()
