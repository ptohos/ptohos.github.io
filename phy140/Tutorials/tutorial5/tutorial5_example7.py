#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Strings revisited

Links:
https://python.land/introduction-to-python/functions
'''
from myFunctions import *

# Define two string variables
name     = "Richard"
surname  = "Feynman"
# Join (concatenate) two strings with the + operator
fullName = name + " " + surname
print( "1) fullName =", fullName, "is of type", type(fullName), sep=" '", end="'.\n")


# Convert (cast) a string to int/float
dd = "4" # "04"
mm = "10"
yy = "2022"
# Print today's date
print(dd, mm, yy, sep="/", end="\n")

# Print tomorrow's date
print(int(dd)+1, mm, yy, sep="/", end="\n")

# More on strings
word = "physics"
print("=== Word", word, "has", len(word), "characters", sep=" ", end=".\n")
for i,c in enumerate(word, 0):
    print("%s | %s" % (c, word[i]) )

print("\n=== Quit!")
quit()
