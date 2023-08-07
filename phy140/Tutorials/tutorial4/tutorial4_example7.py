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

        
def f(x):
    return x+1

def g(x):
    return x + 2

def h(x):
    return x + 3

try:
    msg = "=== Please type integer numbers in range [0, infty]: "
    x = int(input(msg))
except:
    Print("Something went wrong")

Print('x = %s' % (x) )
Print('f(x) = %s' % f(x))
Print('g(x) = %s' % g(x))
Print('h(x) = %s' % h(x))


Print('f ( g( h(x) ) ) = %s' % f( g( h(x) )) )

Print("Quit!")
quit()
