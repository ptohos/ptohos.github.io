#!/usr/bin/python3

'''
Eyresi tou paragontikou enos arithmou
 n! = n*(n-1)*(n-2)*...2*1
O arithmo n prepei na einai thetikos 
akeraios. 
An n=0 tote n!=1
'''

k=int(input("Dwse ton arithmo tou opoioi tha upologisoume to paragontiko "))

if k < 0 :
    print(" Lanthasmeni eisagwgi stoixeiwn")
    print(" Den orizetai to paragontiko arnitikou arithmou")
    exit()

factorial = 1
for fact in range(k,1,-1):
    factorial = factorial * fact

print(" ",k,"! = ",factorial)
exit
