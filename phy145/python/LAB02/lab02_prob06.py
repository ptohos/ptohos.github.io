#!/usr/bin/python3

# Read three numbers
Numbers = int(input("Give me to plithos twn arithmwn "))
if Numbers == 0:
    print("Lanthasmeni eisagwgi stoixeiwn")
    print("Prepei na dwsete to plithos twn arithmwn pou tha eisaxthoun")
    exit()
#
theSum = 0.0      # initialization tou athroismatos twn arithmwn
for inum in range(Numbers) : 
    print("Give me the number",inum+1)
    x = float(input())
    print("O",inum+1,"os arithmos pou dothike einai:",x)
    theSum = theSum + x

average = theSum/Numbers
print("H mesi timi twn",Numbers,"arithmwn pou dothikan einai:",average)

#=============================
# To idio me ti xrisi listas
#=============================
print("===================================")
print("Ta apotelesmata me ti xrisi listas")
print("===================================")
# Read three numbers
Numbers = int(input("Give me to plithos twn arithmwn "))
if Numbers == 0:
    print("Lanthasmeni eisagwgi stoixeiwn")
    print("Prepei na dwsete to plithos twn arithmwn pou tha eisaxthoun")
    exit()
#

TheNumbers=[]   # Dimiourgia mias adeias listas 
for inum in range(Numbers) :   # Me basi to plithos twn arithmwn dimioyrgise
    print("Give me the number",inum+1)
    x = float(input())
    TheNumbers = TheNumbers + [x]  # O + telestis enwnei 2 listes. Tin arxiki
                                   # kai ti lista me 1 stoixeio to x
                                   # Tha mporousame na to kanoume me ti methodo
                                   # append().Tha grafame TheNumbers.append(x) 
    print("O",inum+1,"os arithmos pou dothike einai:",x)

average = sum(TheNumbers)/len(TheNumbers)  # Xrisi sunartisewn sum() kai len()
                                           # gia na broune to athroisma twn
                                           # stoixeiwn tis listas kai tou
                                           # plithous twn stoixeiwn tis listas
print("H mesi timi twn",Numbers,"arithmwn pou dothikan einai:",average)

quit()
