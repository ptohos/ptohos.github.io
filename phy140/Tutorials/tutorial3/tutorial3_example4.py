#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to logical/comparison operators

''' 
myNumber = int(input("Please select a number in the range [0,9]: "))
msg = ""

# If can be used by itself (without else)
if (myNumber == 0):
    msg = "=== A "
    print(msg)
    
if (myNumber != 1):
    msg = "=== B "
    print(msg)
    
if (myNumber < 2):
    msg = "=== C "
    print(msg)

if (myNumber > 4):
    msg = "=== D "
    print(msg)

if (myNumber <= 8):
    msg = "=== E "
    print(msg)
    

myNumber = int(input("Please select another number in the range [0,9]: "))
if (myNumber == 1):
    msg = "=== A "
    print(msg)
elif (myNumber == 2):
    msg = "=== B "
    print(msg)
elif (myNumber <= 6):
    msg = "=== C "
    print(msg)
elif (myNumber < 10):
    msg = "=== D "
    print(msg)
else:
    msg = "==== Number '%d' is out of range!" % (myNumber)
    print(msg)    
    
quit()

