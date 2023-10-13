#!/usr/bin/python3

xup = 20; xlo = 0; dx=0.5
nstps = int((xup-xlo)/dx)
# (a) for loop
a=[]
for i in range(nstps+1):
    a += [i*dx]
print(a)
# (b) list comprehension
a=[x*dx for x in range(nstps+1)]
print(a)
# (c) sunartisi kai map
def f(x):
    return x*dx
a=list(map(f,range(nstps+1)))
print(a)
quit()
