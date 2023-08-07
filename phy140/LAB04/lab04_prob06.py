#!/usr/bin/python3

while True:
    LowVal = int(input("Give the low value of the interval "))
    UpVal = int(input("Give the upper value of the interval "))
    if LowVal >= UpVal :
        print(" Wrong input parameter ")
        print(" Low value of the interval is larger than Upper Value ")
        print(" Make another selection")
    else:
        break    # If everything is ok we break out of the infinite loop 

'''
 Efoson theloyme to athroisma twn akeraiwn apo LowVal
 mexri UpVal, xreiazetai na grapsoume ena loop poy 
 tha arxizei na metra apo LowVal+1 (anoikto diastima) 
 mexri UpVal-1 kai na ayksanei kata monada. Prepei 
 akoma na kratame to plithos twn epanalipsewn wste sto
 telos na upologisoume to meso oro.
'''

isum = 0
count = 0
num = LowVal + 1

while num < UpVal:
    isum = isum + num    # To athroisma twn akeraiwn sto diastima
    count = count + 1    # To plithos twn akeraiwn sto diastima
    num = num + 1        # Auksisi tou arithmoy sto diastima

if count != 0 :
    average = isum/count
else:
    average = 0.0

print("=======================================================")
print(" Athroisma akeraiwn sto diastima (",LowVal,",",UpVal,")")
print(" Brethikan ",count, " akeraioi")
print(" To athroisma tous einai: ", isum)
if count > 0 :
    print(" O mesos oros einai ", average)
else:
    print(" Den yparxei mesos oros")
print("==================================================")

'''
 Paromoia me pio panw alla xrisimopoiwntas for loop
'''
print('2os tropos')
print('Xrisimopoiontas for loop')
print(50*('='))
count = 0
isum = 0
for num in range(LowVal+1, UpVal):
    count = count + 1
    print("O akeraios",count,"enai",num)
    isum = isum + num

if count != 0 :
    average = isum/count
else:
    average = 0.0

print(50*"=")
print(" Athroisma akeraiwn sto diastima (",LowVal,",",UpVal,")")
print(" Brethikan ",count, " akeraioi")
print(" To athroisma tous einai: ", isum)
if count > 0 :
    print(" O mesos oros einai ", average)
else:
    print(" Den yparxei mesos oros")
print(50*("="))

'''
 Paromoia me pio panw alla xrisimopoiwntas numpy
'''
print('3os tropos')
print('Xrisimopoiontas Numpy')
print(50*"=")
import numpy as np
A = np.arange(LowVal+1,UpVal)
print(" Athroisma akeraiwn sto diastima (",LowVal,",",UpVal,")")
print(" Brethikan ",A.size, " akeraioi")
print(" To athroisma tous einai: ", A.sum())
print(" O mesos oros einai ", A.mean())
print(50*"=")
