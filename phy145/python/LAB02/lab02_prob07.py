#!/usr/bin/python3


LowVal = int(input("Give the low value of the interval "))
UpVal = int(input("Give the upper value of the interval "))

if LowVal >= UpVal :
    print(" Wrong input parameter ")
    print(" Low value of the interval is larger than Upper Value ")
    print(" Make another selection")
    exit()

'''
 Efoson theloyme to athroisma twn akeraiwn apo LowVal
 mexri UpVal, xreiazetai na grapsoume ena brogxo poy 
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
print(" Athroisma akeraiwn sto diastima (",LowVal,UpVal,")")
print(" Brethikan ",count, " akeraioi")
print(" To athroisma tous einai: ", isum)
if count > 0 :
    print(" O mesos oros einai ", average)
else:
    print(" Den yparxei mesos oros")
print("=======================================================")

# Paromoia me pio panw alla xrisimopoiwntas for loop
count = 0
isum = 0
for num in range(LowVal+1, UpVal):
    count = count + 1
    isum = isum + num

if count != 0 :
    average = isum/count
else:
    average = 0.0

print("=======================================================")
print(" Athroisma akeraiwn sto diastima (",LowVal,UpVal,")")
print(" Brethikan ",count, " akeraioi")
print(" To athroisma tous einai: ", isum)
if count > 0 :
    print(" O mesos oros einai ", average)
else:
    print(" Den yparxei mesos oros")
print("=======================================================")

    
