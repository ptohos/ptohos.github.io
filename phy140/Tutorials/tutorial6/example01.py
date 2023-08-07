#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
The split() method for strings that takes the generic form:
str.split( sep=" ", maxsplit=-1 )


Links:
https://www.w3schools.com/python/ref_string_split.asp
'''
# Define a string variables
phrase = "It's.... Monty Python's Flying Circus"

# Let's try some split settings
print("=== default split (1)")
mySplit = phrase.split()
print(mySplit)
print(type(mySplit))
print(len(mySplit))

print("\n=== one-space split (1)")
mySplit = phrase.split(" ", 1)
print(mySplit)
print(type(mySplit))
print(len(mySplit))


print("\n=== two-spaces split (1)")
mySplit = phrase.split(" ", 2)
print(mySplit)
print(type(mySplit))
print(len(mySplit))


# Let's now change the splitting variable
print("\n=== default y split (2)")
mySplit = phrase.split("y", -1)
print(mySplit)
print(type(mySplit))
print(len(mySplit))

print("\n=== one-space split (2)")
mySplit = phrase.split("y", +1)
print(mySplit)`
print(type(mySplit))
print(len(mySplit))


print("\n=== two-spaces split (2)")
mySplit = phrase.split("y", +2)
print(mySplit)
print(type(mySplit))
print(len(mySplit))


# Let's finish off with another two example
print("\n=== default split (3)")
mySplit = phrase.split("...", -1)
print(mySplit)

# Let's finish off with another two example
print("\n=== default split (4)")
mySplit = phrase.split(".", -1) # *reward!
print(mySplit)

print("\n=== Quit!")
quit()
