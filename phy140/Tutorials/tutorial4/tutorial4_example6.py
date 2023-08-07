#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to functions

Links:
https://www.w3schools.com/python/python_operators.asp
https://www.tutorialspoint.com/python3/python_functions.htm
https://www.w3schools.com/python/trypython.asp?filename=demo_oper_mod

'''
def Print(msg, header=True):
    '''
    msg ....: string to be printed
    
    return..: nothing
    '''
    if (header):
        print("=== example5.py:\n\t", msg)
    else:
        print("\t", msg)


def factorial(x):
    '''
    returns the factorial of positive integer number  x 

    x: positive integer number (>

    return: integer 
    '''
    if (x < 0):
        msg = "Cannot evaluate factorial of negative numbers (undefined)"
        raise Exception(msg)
    
    if (x in [0, 1]):
        return 1
    else:
        return x*factorial(x-1) # function calls itself


def factorialAlt(x):
    '''
    As shown in Lecture 04, page 20
    '''
    f = 1.0
    for k in range(1, n+1):
        f*=k
    return f


#Print("Please type integer numbers in range [0, infty]")
try:
    msg = "=== Please type integer numbers in range [0, infty]: "
    x = int(input(msg))
    Print("factorial(%d) = %d" % (x, factorial(x)))
except:
    Print("Something went wrong. Please see below the docstrings of the %s function!" % (factorial.__name__))
    Print(factorial.__doc__)
    #help(factorial)    

Print("Quit!")
quit()
