#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to local and global variables

Links:
https://python.land/introduction-to-python/functions
https://en.wikipedia.org/wiki/Richard_Feynman
https://en.wikipedia.org/wiki/Democritus
'''
from myFunctions import *

name     = "Richard"
surname  = "Feynman"
fullName = name + " " + surname
say_hi(fullName, 3, 6, "PHYS-140")

def getName(n, s):
    fullName = n + " " + s
    otherName = "Democritus" # local variable is undefined outside scope of this function
    return fullName # this local variable is NOT related to the global variable 'fullName'

def changeGlobalVariable(newName="Dire Straits"):
    global fullName
    # global variable is now accessible from anywhere in our script
    fullName = newName 


print( "=== Full name is", fullName, sep=" '", end="'.\n")
print( "=== Full name is", getName("Albert", "Einstein"), sep=" '", end="'.\n")
print( "=== Full name is still", fullName, sep=" '", end="'!!!\n")

try:
    print( "=== otherName", otherName)
except:
    print( "=== Cannot print undefined variable 'otherName'")


print( "\n=== Full name has not changed yet. It still is", fullName, sep=" '", end="'.\n")

changeGlobalVariable(newName="Dire Straits")
print( "=== After declaring as global variable, the full name is", fullName, sep=" '", end="'.\n")

    
print("\n=== Quit!")
quit()
