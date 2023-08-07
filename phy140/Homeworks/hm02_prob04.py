#!/usr/bin/python3

''' Pinakas dinatwn apotelesmatwn se morfi listas
Apotelesma[0][0] = 0   # petra - petra      isopalia
Apotelesma[0][1] = 1   # petra - psalidi    kerdizei o 1
Apotelesma[0][2] = 2   # petra - xarti      kerdizei o 2

Apotelesma[1][0] = 2   # psalidi - petra    kerdizei o 2
Apotelesma[1][1] = 0   # psalidi - psalidi  isopalia
Apotelesma[1][2] = 1   # psalidi - xarti    kerdizei o 1

Apotelesma[2][0] = 1   # xarti - petra      kerdizei o 1
Apotelesma[2][1] = 2   # xarti - psalidi    kerdizei o 2
Apotelesma[2][2] = 0   # xarti - xarti      isopalia
'''
Apotelesma = [ [0, 1, 2], [2, 0, 1], [1, 2, 0] ]

player1 = input("Epilogi paikti 1 ? ")
if player1 == 'petra' :
    ch1 = 0
elif player1 == 'psalidi' :
    ch1 = 1
elif player1 == 'xarti' :
    ch1 = 2
else:
    print("Wrong choice is made - Please try again")
    quit()

player2 = input("Epilogi paikti 2 ? ")
if player2 == 'petra' :
    ch2 = 0
elif player2 == 'psalidi' :
    ch2 = 1
elif player2 == 'xarti' :
    ch2 = 2
else:
    print("Wrong choice is made - Please try again")
    quit()

if ch1 == ch2 :
    print("Isopalia")
else:
    print(" O paiktis %d kerdizei" % Apotelesma[ch1][ch2])

print()
print("================================")
print("Try the game with random choices")
print("================================")
from random import random
choices = ['petra','psalidi','xarti']
ch1 = int(3*random())     # Metatropi se akeraio arithmo metaksy 0 kai 2
print("Epilogi gia ton Paikti 1 : %s"%choices[ch1])
ch2 = int(3*random())
print("Epilogi gia ton Paikti 2: %s "%choices[ch2])

if ch1 == ch2 :
    print("Isopalia")
else:
    print(" O paiktis %d kerdizei" % Apotelesma[ch1][ch2])

