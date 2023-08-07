#!/usr/bin/python3

npow = int(input("Give the max exponent "))

for i in range(npow):
    print("2**",i,' is equal to ',2**i)

'''
 kai xrisimopoiontas format
'''
print("Me format")
for i in range(npow):
    print("2**%2d is equal to %4d"%(i,2**i))
    
