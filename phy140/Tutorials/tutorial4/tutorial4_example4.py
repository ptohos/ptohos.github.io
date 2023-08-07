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
https://www.w3schools.com/python/python_for_loops.asp

'''
def CelciusToFarenheit(C):
    '''
    C ....: temperature in degrees Celcius
    
    return: temperature in degrees Farenheit
    '''
    F = (C*9/5) + 32
    return F

# Declare empty lists
Celcius=[]
print("\n=== Please provide 10 temperature values in degrees Celcius: ")    
counter = 1
while len(Celcius) < 10:
    try:
        Celcius.append(float(input("\t%d) " % (counter))) )
        counter+=1
    except:
        print("\tInvalid temperature value. Please try again!")

    
Farenheit = [CelciusToFarenheit(C) for C in Celcius]

print("\n=== Conversion table:\n {:>8} {:>8}".format("(C)", "(F)"))
for i in range(0, len(Celcius), 1):
    print('{:8.1f} {:8.1f}'.format(Celcius[i], Farenheit[i]))

    

print("\n=== Quit!")
quit()

