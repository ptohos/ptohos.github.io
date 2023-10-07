#!/usr/bin/python3

import numpy as np

def extract_lesser(mylist,N):
    newlist=[]
    for i in mylist:
        if i< N:
            newlist.append(i)
    return newlist

#Kurio programma
N=29
infile=open("mylist.txt",'w')
infile.write(19*'{:2d}\n'.format(2,12,8,28,3,23,16,32,25,-1,6,9,-2,34,48,21,31,24,43))
infile.close()
mylist=[]
with open("mylist.txt",'r') as fp:
    for line in fp:
        mylist.append(int(line))
fp.close()

print(mylist)
nlist=extract_lesser(mylist,N)
print("Oi duo listes einai:\n")
mylist=np.array(nlist)
nlist=np.array(nlist)
for i in mylist:
    match = False
    for j in nlist:
        if i == j :
            print('{:2d}     {:2d}'.format(i,j))
            match = True
            break
    if match != True:
        print('{:2d}'.format(i))
quit()


    
