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


def GetLargestPrime(minNum, maxNum):
    '''
    returns largest prime number in range [minNum, maxNum]

    minNum: smallest integer to use in search range
    maxNum: largest integer to use in search range
    
    return: integer 
    '''
    if (minNum < 2 or maxNum < 2):
        msg = "Invalid search range [%d, %d]. The smallest integer is 2!" % (minNum, maxNum)
        raise Exception(msg)

    
    if (minNum > maxNum):
        msg = "The maximum integer (=%d) must have a larger value than the minimum integer (=%d)" (maxNum, minNum)
        raise Exception(msg)

    # Declare variables
    myPrimes = []
    i = minNum #2

    # Outside while-loop
    while(i <= maxNum):
        j = minNum

        # Nested while-loop (only need to consider numbers halfway through the range)
        while(j <= (i/j)):

            # Use modulo arithmetic operator to see if i is perfectly divisible by j
            if not(i % j):
                # division remainder is 0 => i divisible by j => not a prime!
                break
            # Increment index of nested-loop  (until you find a prime number)
            j = j + 1

        # Check if j is a prime. If yes append to the list of primes
        if (j > i/j):
            if 0:
                Print("%d is prime!" % (i))
            myPrimes.append(i)

        # Increment index for outside loop
        i = i + 1
        
    Print("List of prime numbers found: %s" % (myPrimes))
    return myPrimes[-1]



print("\n=== Please type two integer numbers, i and j, so that i < j: ")    
try:
    minNum = (int(input("\tMinimum: ")))
    maxNum = (int(input("\tMaximum: ")))
    Print("Largest prime in range [%d, %d] is %d" % (minNum, maxNum, GetLargestPrime(minNum, maxNum)))
except:
    Print("Something went wrong. Please see below the docstrings of the %s function!" % (GetLargestPrime.__name__))
    Print(GetLargestPrime.__doc__)
    help(GetLargestPrime)    

Print("Quit!")
quit()
