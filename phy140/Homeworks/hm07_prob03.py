#!/usr/bin/python3

'''
H paragwgos einai: dy/dt = y*(1-y)/(2*y-1)
Mas dinetai oti i analytiki lysi einai
y(t) = 1/2 + sqrt(1/4 - 5/36*exp(-t)]
Epomenws i paragwgos meta apo prakseis
tha mporouse na grafei ws
y'(t) = 5/36 * exp(-t)/sqrt(1-5/9*exp(-t))
'''
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

t=Symbol('t')
f=5*exp(-t)/(36*sqrt(1-5/9*exp(-t)))
ff=integrate(f,(t,0,t))     # Oloklirwma ws pros t apo 0 ws t
aa=lambdify(t,ff,'numpy')
print("The integral with sympy is %6.4f"%aa(2))
#
def myfunc(t):              # Synartisi oloklirwsis 
    return 5*exp(-t)/(36*sqrt(1-5/9*exp(-t)))

def analytic(t):
    return 1/2 + sqrt(1/4 - 5*exp(-t)/36)

def midpoint(f,lower,upper,dx):
    n = int((upper-lower)/dx)
    result = 0
    for i in range(n):
        result += f((lower+dx/2.0) + i*dx)
    result *= dx
    return result

def euler(lower,upper,dt):
    Y, T, Yth = [], [], []
    t=lower
    y=5/6
    while t <= upper:
        Y +=[y]
        T +=[t]
        Yth += [0.5 + np.sqrt(0.25 - 5/36 * np.exp(-t))]
        dydt = y*(1-y)/(2*y-1) 
        y += dydt * dt
        t += dt
    return Y, T, Yth

low_x = 0
hi_x = 2
#========================
# (b) Grafiki parastasi
#========================
dx = 0.1
mid_integral = midpoint(myfunc,low_x,hi_x,dx)
print("The integral with midpoint method is %6.4f for dx=%2.1f"%(mid_integral,dx))

YY1,TT1,Yanal1 = euler(low_x,hi_x,dx)
print("The integral with the Euler method is %6.4f for dx=%2.1f"%((YY1[-1]-YY1[0]),dx))

dx = 0.0001
mid_integral = midpoint(myfunc,low_x,hi_x,dx)
print("The integral with midpoint method is %6.4f for dx=%5.4f"%(mid_integral,dx))
YY2,TT2,Yanal2 = euler(low_x,hi_x,dx)
print("The integral with the Euler method is %6.4f for dx=%5.4f"%((YY2[-1]-YY2[0]),dx))
#======================
# (g) Error
#======================
dx = 0.1
error = []
xdx = []
while dx >= 0.0001:
    yy,tt,yanal = euler(low_x,hi_x,dx)
    err = np.abs(yy[-1]-yanal[-1])/yanal[-1]
    error +=[err]
    xdx +=[dx]
    dx /=5

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.plot(TT1,Yanal1,'-')
plt.plot(TT1,YY1,'b--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.text(0.17,0.975,'Analytic')
plt.hlines(0.977, 0.0,0.15,color='k',linestyle='solid')
plt.text(0.17,0.961,'Euler - dx=0.1')
plt.hlines(0.963,0.0,0.15,color='b',linestyle='dashed')

plt.grid(True)
plt.subplot(1,2,2)
plt.plot(TT2,Yanal2,'-')
plt.plot(TT2,YY2,'b--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.text(0.17,0.975,'Analytic')
plt.hlines(0.977, 0.0,0.15,color='k',linestyle='solid')
plt.text(0.17,0.961,'Euler - dx=0.0001')
plt.hlines(0.963,0.0,0.15,color='b',linestyle='dashed')
plt.grid(True)
plt.tight_layout()
plt.show()
#
plt.figure(figsize=(6,4))
plt.loglog(xdx,error,'b-')
plt.xlabel('dx')
plt.ylabel(r'Error = $\frac{|Analytical - Euler|}{Analytical}$')
plt.show()
