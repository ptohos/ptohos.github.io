#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Simple example of function defintion. Example2 will built on this to understand importing python modules

Links:
https://python.land/introduction-to-python/functions
'''
def powerN(x, exp):
    #print("=== Evaluating x**exp (x=%s is of type %s, exp=%s is of type %s" % (x, type(x), exp, type(exp)) )
    return x**exp

if 0:
    # Get string input from user
    num = int(input("=== Please give the number (integer): "))   # if input is not an int then error here
    exp = int(input("=== Please give the exponent (integer): ")) # if input is not an int then error here
    try:
        numExp = powerN( num, exp)
        print("=== %d**(%d) = %d" % (num, exp, numExp) )
    except:
        print("=== Something went wrong!")
else:
    # what happens if we decide to cast the inputs at a later stage when the function is called?
    # Does it behave differently (better/worse) if you provide a character as input (instead of integer)?
    
    # Get string input from user
    num = input("=== Please give the number (integer): ")    # if input is not an int no error here
    exp = input("=== Please give the exponent (integer): ")  # if input is not an int no error here
    try:
        numExp = powerN( int(num), int(exp) ) 
        print("=== %d**(%d) = %d" % (int(num), int(exp), numExp) )
    except:
        print("=== Something went wrong!")   # if input is not an int the error is found here
        
print("=== Quit!")
quit()
