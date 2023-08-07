#!/usr/bin/python3

import numpy as np

timelapse = int(input("Give the time in hours "))

#
hours = timelapse%24      # To upoloipo tis sdiairesis me 24 (wres/imera) dinei
                          # to tmima tou xronikou diastimatos pou de symplirwnei
                          # mia imera.
ndays = timelapse//24     # To piliko tis diairesis me 24 tha dwsei poses imeres
                          # sunolika uparxoun sto xroniko diastima
months = ndays//30        # To piliko tis diairesis tou arithmou twn imerwn
                          # me 30 tha dwsei ton arithmos twn minwn
ndays = ndays - months*30 # To upoloipo tha dwsei poses meres den einai meros
                          # tou mina 
print("To xroniko diastima %d wrwn antistoixeis %d mines %d meres kai %d wres"
      %(timelapse,months,ndays,hours))

print("Good bye")
