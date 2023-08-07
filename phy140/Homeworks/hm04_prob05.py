#!/usr/bin/python3

import matplotlib.pyplot as plt

def func(t,a,b):
    return a*t + b

def find_error(a, b):
    E = 0
    for i in range(len(time)):
        E += (func(time[i],a,b) - data[i])**2 
    return E

def interactive_line_fit():
    one_more = True
    while one_more:
        a = float(input('Give a: '))
        b = float(input('Give b: '))
        print('The error is %g '% find_error(a, b)  )
        y = []
        for j in range(len(time)):
            y += [func(time[j],a,b)]
        plt.plot(time,y)
        plt.plot(time,data,'*')
        plt.xlabel('Time (s)')
        plt.ylabel('y (stars) and straight line f(t)')
        plt.show()
        answer = input('Do you want another fit (y/n)? ')
        if answer == 'n' or answer == 'N' :
            one_more = False

def grid_line_fit(amn,amx,bmn,bmx,delta):
    alow = amn
    blow = bmn
    error_min = 1E9
    while alow <= amx:
        blow = bmn
        while blow <= bmx:
            error = find_error(alow,blow)
            if error <= error_min:
                error_min = error
                aopt = alow
                bopt = blow
            blow +=delta
        alow +=delta
    print('Min error found %.6f'%error_min)
    print('Optimal value of a: %.3f'%aopt)
    print('Optimal value of b: %.3f'%bopt)
    y = []
    for j in range(len(time)):
        y += [ func(time[j],aopt,bopt) ]
    
    plt.plot(time,y)
    plt.plot(time,data,'*')
    plt.xlabel('Time (s)')
    plt.ylabel('y (stars) and straight line f(t)')
    plt.show()

def read_data():
    xx = []
    yy = []
    inpfile = open('measurements.dat','r')
    for lines in inpfile:
        try:
            x,y = lines.split()
            xx += [float(x)]
            yy += [float(y)]
        except:
            continue
    return xx, yy

time, data = read_data()

interactive_line_fit()

print(" One could give a from 0 to 2 and b for -5 to 2 with a step of 0.001 ")
amin = float(input("Lower value of a to search for error minimization "))
amax = float(input("Upper value of a to search for error minimization "))
bmin = float(input("Lower value of b to search for error minimization "))
bmax = float(input("Upper value of b to search for error minimization "))
delta = float(input("Step to use to change a and b values "))

grid_line_fit(amin,amax,bmin,bmax,delta)


               
