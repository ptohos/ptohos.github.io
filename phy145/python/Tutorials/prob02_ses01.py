#!/usr/bin/python3

def func(X, Y, Z):
    tot = 0
    lowv = X
    higv = Y
    if X > Y:
        lowv = Y
        higv = X
    for num in range(lowv,higv+1):
            if num%M == 0:
                tot += 1
    return tot

a,b,c = input("Dose arithmous: ").split(",")
a = int(a)
b = int(b)
c = int(c)
res = func(a,b,c)

print(res)

exit()
