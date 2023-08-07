#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
More on string manipulation (find, replace)


Links:
'''
import numpy as np

# Define two string variables
phrase1 = "It's.... Monty Python's Flying Circus"

# Return the index of the FIRST match (start from 0!)
print(phrase1.find("."))

# If no match is found returns -1
print(phrase1.find("!"))

# Lower/Upper-case letters
print(phrase1.lower())
print(phrase1.upper())

# The original string is UNCHANGED (not assigned to a variaible)
print(phrase1)

# Case-insensitive searches
if 0:
    phrase2 = input("Please type any character or string. Will look for lower or upper case 'A': ")
    match   = []
    for l in phrase3:
        if l.lower() == "a":
            match.append(l)
    print("=== Found %d matches for letter 'A' in input '%s'" % (len(match)), phrase3, end="!\n")


print("=== Showing the replace function ('/' with '-')")
dateOld = "04/10/2022"
dateNew = dateOld.replace("/", "-")
print("\tdateOld= %s\n\tdateNew = %s" % (dateOld, dateNew) )


print("=== Showing the usage of methods lstrip(), rstrip(), strip(), and startwith()")
phrase3 = "     --> And Now for Something Completely Different<--       "
print("=== phrase3 = ", phrase3)
print("=== phrase3.lstrip()", phrase3.lstrip())
print("=== phrase3.rstrip()", phrase3.rstrip())
print("=== phrase3.strip)()", phrase3.strip())

name = "Albert Einstein"
print(name.startswith("A"))
print(name.startswith("a"))
print(name.startswith("Albe"))
    
print("\n=== Quit!")
quit()
