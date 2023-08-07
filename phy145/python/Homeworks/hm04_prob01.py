#!/usr/bin/env python3

"""
To programma elegxei an enas arithmos pou dinetai 
periexei ena epithimito psifio 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import numpy as np
import random as rng

def isSuccessful(number, WantedDigit=0):
    """H sunartisi elegxei an kapoios arithmos 
       periexei to epithymito psifio.
    Orismata:
       number - tyxaios thetikos arithmos - type int  
       WantedDigit - psifio (default is 0) - type int
    """
    while number > 0:
        # Apodomisi tou arithmou psifio pros psifio
        if number % 10 == WantedDigit:
            return True     # vrethike kai exodos apo to loop & synartisi
        else:
            number //= 10   
 
    return False
 
def isSuccessfulStr(numberStr, WantedDigit= '0'):
    """Elegxos an o arithmos se string format periexei to psifio
    Orismata:
       numberStr -  ena arithmitiko string
       magicDigit - ena string enos psifiou (default is '0')
    """
    return WantedDigit in numberStr # Eksetasi tou numberStr xaraktira
                                    # pros xaraktira me ti xrisi tis in function
                                    
 
def main():
    ThisDigit = int(input("Input the desired digit "))
    filename  = input("Give the output file name ")
    outfile = open(filename,'w')
    SuccessCount = 0
    for numb in range(100):
        anumber = rng.randint(1,123456789)
        if isSuccessful(anumber,ThisDigit):
            print('{} contains the desired digit'.format(anumber))
            outfile.write('%10d'%anumber)
            SuccessCount +=1
        else:
            print('{} doe NOT contain the desired digit'.format(anumber))
 
        if isSuccessfulStr(str(anumber), str(ThisDigit)):
            print('{} contains the desired digit'.format(anumber))
        else:
            print('{} does NOT contain the desired digit'.format(anumber))
    print('Out of 100 random numbers, %4d contain the digit %1d'%(SuccessCount,
                                                                  ThisDigit))
    outfile.close()
    
# Run the main function
main()
 
