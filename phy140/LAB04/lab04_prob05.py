#!/usr/bin/python3

'''
 A - erotima
'''
num = int(input("Give a number: "))
divisors = 0
for i in range(1,num+1):
    if num % i == 0:
        divisors += 1
print("The number", num, "has",divisors, "divisors.")

print(40*('='))
print("Erwtima B")
print(40*('='))
print("Finding in the range [1,10000] the Number with Max number of devisors")
print("Pease wait...")
maxDivisors = 1;  # 1 is divided by 1 
numWithMax = 1;
"""
Gia kathe N apo to 2 ews to 10000 briskoume tous diairetes tou
An o N exei perissoterous diairetes apo ton megisto arithmo pou
exoume vrei mexri ton N-1 tote ananewnoume to megisto plithos
twn diairetwn kathws kai ton arithmo pou exei to megisto plithos
diairetwn
"""
       
numWithMax = []  # Dimiourgia kenis listas gia na kratisoume diairetes 
                 # me ton megisto arithmo diairetwn 
for N in range(2,10001):
    divisorCount = 0;
    for D in range(1,N+1):   #Count the divisors of N. as in part A
        if N % D == 0:
            divisorCount += 1
           
    if divisorCount >= maxDivisors:    # Update the maxDivisors if we found more
        if divisorCount > maxDivisors:
            numWithMax = []            # Reset the list if found more divisors
        numWithMax += [N]
        maxDivisors = divisorCount
              
print("In the range [1, 10000]")
print("The maximum number of divisors is", maxDivisors);
if len(numWithMax)==1 :
    print("Numbers with" , maxDivisors , "divisors is" , numWithMax[0]);
else:
    # Xrisimopoioume ton *List gia na perasei to print e ola ta stoixeia tis
    # listas kai na ta typwsei kratontas duo kena metaksu tous me to sep
    print("Numbers with", maxDivisors, "divisors are", *numWithMax, sep=',  ')
# Possible answers:
# a) 7560
# b) 9240
# with 64 divisors
