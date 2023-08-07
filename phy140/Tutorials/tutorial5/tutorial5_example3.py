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
https://en.wikipedia.org/wiki/Paraskevas_Sphicas
https://www.youtube.com/watch?v=cYyOHqupRDU
'''
import myFunctions as f

f.say_hi("Paris Sphicas", 3, 4, "PHYS-140")

# Get string input from user
num, exp = f.getTwoInts()
try:
    numExp = f.powerN( num, exp)
    print("=== powerN(%d, %d) = %d" % (num, exp, numExp) )
except:
    print("=== Something went wrong!")
        
# Can repear procedure as many times as we like
print("\n=== Another example")
num, exp = f.getTwoInts("Please insert value (int) for x: ", "Please insert value (int) for exponent: ", )
print("=== powerN(%d, %d) = %d" % (num, exp, f.powerN( num, exp)) )


print("=== Quit!")
quit()
