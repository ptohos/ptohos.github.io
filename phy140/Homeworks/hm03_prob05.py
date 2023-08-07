#!/usr/bin/python3

def interpolate(y, x, x_int):
    '''Uses linear interpolate to find intermediate y
             y_int - y(jd) = slope * [x_int - x(jd)]
             y_int = y(jd) + slope * [x_int - x(jd)]
       with slope [y(jd+1)-y(jd)]/[x(jd+1)-x(jd)]
    '''
    jk = -1
    for j in range(len(x)-1):
        if x[j] < x_int and x_int < x[j+1] :     # interval that includes t
           jk = j
    if jk < 0:
        print("Value of x_int is not in the interval")
        return -999
    delta_x = x[jk+1] - x[jk]
    delta_y = y[jk+1] - y[jk]
    return y[jk] + (delta_y/delta_x)*(x_int - x[jk])

def find_y():
    '''Repeatdly finds y at t by inrerpolation'''
    print('For time t in the interval[0,%d]...'%N)
    x_des = float(input("give your desired x_desire >0: "))
    while x_des >=0 :
        print("y(x_desire) = %g"%interpolate(y,x,x_des))
        x_des = float(input("Give new x_desire (to stop, enter x_desire < 0): "))


N = 5               # Number of measurements
y=[]; x=[]
for i in range(N):
    y += [0]
    x += [i]
              
y[0] = 4.4; y[1] = 2.0; y[2] = 11.0;
y[3] = 21.5 ; y[4] = 7.5

find_y()
