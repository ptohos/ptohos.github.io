#!/usr/bin/python3

N2give=int(input("Give the number of integers to read "))
iread = 0
mynumbers = []           # Dimiourgia mias kenis listas
mysqrnumbers = []        # Dimiourgia mias kenis listas 
while iread < N2give:
    s = "Give the %d integer "%(iread)
    numb = int(input(s))
    mynumbers.append(numb)         # eisagwgi tou arithmou sti lista
    mysqrnumbers.append(numb*numb) # to tetragwno
    iread += 1

'''
An ithela na tous typwsw
'''
for j in range(len(mynumbers)):   # vriskoume to mikos tis list
    print("{:5d} {:8d}".format(mynumbers[j],mysqrnumbers[j]))
