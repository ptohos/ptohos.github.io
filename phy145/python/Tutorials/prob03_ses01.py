#!/usr/bin/python3

def switcheroo(num):
    n1 = num//100
    n2 = (num%100)//10
    n3 = (num%100)%10
    
    res = str(n3) + str(n2) + str(n1)
    
    return res

i = int(input("Dose tripsifio arithmo: "))
ans = switcheroo(i)

print(ans)

exit()
