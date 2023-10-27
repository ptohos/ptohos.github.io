#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

filename = 'lab07_motion.dat'
infile = open(filename,'r')
X, Y = [], []
for line in infile:
    try:
        x,y = line.strip().split()
        X +=[float(x)]
        Y +=[float(y)]
    except:
        print("Problem with line:",line)
        continue
infile.close()

plt.figure(figsize=(6,6))
plt.plot(X,Y,'bo')
plt.show()

plt.figure(figsize=(6,6))
plt.loglog(X,Y,'bo')
plt.xlabel('time, t(sec)')
plt.ylabel('position, x(m)')
plt.xlim(0.1,100)
plt.ylim(0.1,10000)
plt.grid(True)
plt.show()

'''
Xrisi twn simeiwn (5,10) kai (50,1000) gia ton upologismo
tis klisis. Ws trito simeio to (15,90)
'''
slope = (np.log(1000) - np.log(10))/(np.log(50)-np.log(5))
intercept = np.log(90) - slope*np.log(15)

'''
Exoume tin eksiswsi log(y)=log(intercept) + klisi*log(x)=>
log(y)-log(intercept) = klisi*log(x) => log(y/intercept)=klisi*log(x)=>
y/intercept  = x^klisi=>  y = intercept * x^klisi

Dimiourgoume ton ajona x kai katopin tha prepei na
paroume to y = e^[intercept+klisi*log(x)].
H timi tis tetagmenis (intercept) einai: y0 = exp(intercept)
kai sumbainei gia log(X)=0 diladi X=1
'''
newX = np.arange(0.1,100.1,0.1)
newY = np.exp(intercept)* newX**slope

Yintercept = np.exp(intercept)
print('The intercept is :',Yintercept)
plt.figure(figsize=(6,6))
plt.loglog(X,Y,'bo')
plt.loglog(newX,newY,'r-',lw=2)
plt.xlabel('time, t(sec)')
plt.ylabel('position, x(m)')
plt.xlim(0.1,100)
plt.ylim(0.1,10000)
plt.axvline(x=1, color='green',linestyle='--')
plt.axhline(y=Yintercept,color='green',linestyle='--')
xin=1
yin=Yintercept
plt.plot(xin,yin,'gs')
plt.text(1.3,0.25,'Intercept(%2.1f,%4.2f)'%(1,yin))
plt.text(10,30,r'$Y(X)=e^{intercept}*x^{slope}$')
plt.text(10,15,r'$Y(X)=%3.1f X^{%3.1f}$'%(yin,slope))
plt.grid(True)

plt.show()

