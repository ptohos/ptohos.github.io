#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Strings revisited. A more in-depth look

Links:
https://www.w3schools.com/python/python_ref_string.asp
https://www.pythonforbeginners.com/basics/string-manipulation-in-python
'''
from myFunctions import *

# Define two string variables
phrase1 = "It's.... Monty Python's Flying Circus"
phrase2 = "And Now for Something Completely Different"

# String slicing
print("=== ", phrase1, end="\n")
print("=== ", phrase1[0:], end="\n")     # same. default last position is position of last character

print("=== ", phrase1[0:-1], end="\n")   # without last letter
print("=== ", phrase1[:-6], end="\n")    # without last word. default start position is 0
print("=== ", phrase1[9:], end="\n")     # without first word
print("=== ", phrase1[9:-16], end="\n")  # first two words


print("\n=== Casting to int/float: ")
piMinusOne = "2.14159"
try:
    print("\tPi = ", float(piMinusOne) + 1.0)
except:
    print("=== ERROR!\n\tSomething went wrong")

try:
    print("\tPi = ", int(piMinusOne) + 1.0)
except:
    print("=== ERROR!\n\tCannot convert string with decimal into integer!")


print("\n=== Use of 'in' and 'not in' operators (strings)")
print("." in phrase2)
print("." not in phrase2)

print("\n=== Use of 'in' and 'not in' operators (lists)")
print(1 in [0, 2, 4, 6, 8, 10])
print("a" in ["Albert", "Eistein", "B"])
print("B" in ["Albert", "Eistein", "B"])


print("\n=== Quit!")
quit()
