#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x example1.py
   python3 example1.py

Usage (v2):
python3 
import example1.py

Description:
Introduction to logical/comparison operators

''' 
myNumber = int(input("Please select a number in the range [0,2]: "))
msg = ""

# If can be used by itself (without else)
if (myNumber == 0):
    msg = "=== Zeroth law of thermodynamics:\n\tIf two bodies, A and B, are in thermal equilibrium with another body C, then these two bodies are also in thermal equilibrium with each another." 
    print(msg)

if (myNumber == 1):
    msg = "=== First law of thermodynamics:\n\tThe total energy of an isolated system is constant; energy can be transformed from one form to another, but neither created nor destroyed."
    print(msg)
    
if (myNumber == 2):
    msg = "=== Second law of thermodynamics:\n\tHeat does not spontaneously pass from a colder to a hotter body."
    print(msg)
    
#print(msg)    

quit()

