#!/usr/bin/python3


num = int(input("Dose tripsifio arithmo: "))
n1 = num//100
n2 = (num%100)//10
n3 = (num%100)%10

res = str(n3) + str(n2) + str(n1)
print(res)

exit()
