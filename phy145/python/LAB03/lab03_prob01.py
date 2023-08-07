#!/usr/bin/python3

import numpy as np

# Give the name of the file to be read
filename = input("Enter the filename ")

file2read=open(filename,'r')   # open a file to read and assign a file handler

count = 0
numbers = []                   # Dimiourgia mias kenis listas gia apothikeusi
                               # twn arithmwn
for lines in file2read:        # anagnwsi toy file grammi grammi
    count += 1
    numb = lines.strip()       # afairesi olwn twn kenwn
    try:
        numb = float(numb)     # metatropi se arithmo
    except:
        print("Mi arithmitiko stoixeio")
        continue               # Anagnwsi tis epomenis grammis
    numbers +=[numb]           # Ayksisi tis list numbers me tin eisagwgi tou
                               # arithmoy sto telos tis listas. Tha mporouse
                               # na gine kai me tin entoli numbers.append(numb)

file2read.close()              # Kleisimo toy arxeiou meta tin anagnwsi
print('To arxeio periexei %d grammes' % count)
print('kai diabastikan %d noumera\n' % len(numbers))
print('H lista twn arithmwn pou diavastikan apo to arxeio einai:\n',numbers)
print('H lista se anapodi seira einai:\n',numbers[::-1])

#======================
# Me xrisi np methodwn
#======================
NPnumbers = np.loadtxt(filename,usecols=0)  # Anagnwsi tou arxeiou kai eisagwgi
                                            # tis prwtis stilis ston NP array
                                            # NPnumbers
print('\nDiabastikan %d noumera' % len(NPnumbers))
print('H lista twn arithmwn pou diavastikan apo o arxeio einai:\n',NPnumbers)
print('H lista se anapodi seira einai:\n',NPnumbers[::-1])
