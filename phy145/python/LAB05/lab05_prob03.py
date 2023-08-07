#!/usr/bin/python3

def averg(*args):
    total = 0
    for i in args:
        total += i
    return len(args), total/len(args)

ntot, average = averg(1,2,3,4)
print('The Average of the %d numbers is:%5.2f' % (ntot,average))

