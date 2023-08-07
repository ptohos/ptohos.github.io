import numpy as np
import matplotlib.pyplot as plt
y1 = lambda x: np.exp(-x)*np.sin(x)
y2 = lambda x: np.cos(x)
y3 = lambda x: np.exp(-x)*np.sin(x) - np.cos(x)
xv = np.arange(0,2.1,0.01)
'''
x=[]
y1=[]
y2=[]
y3=[]
for i in range(101):
    xv = -6 + (i-1)*0.1
    x.append(xv)
    y1.append(5+4*xv-np.exp(xv))
    y2.append(5+4*xv)
    y3.append(np.exp(xv))
'''
plt.figure(num=None,figsize=(12,6),dpi=80,facecolor='w',edgecolor='k')
plt.subplot(121)
plt.plot(xv,y1(xv),xv,y2(xv))
plt.grid(True)
plt.axis([0,2.,-0.5,1.1])
plt.text(0.5,0.35,r'$f1(x)=e^{-x}sin(x)$')
plt.text(0.2,1.0,r'$f2(x)=cos(x)$')
plt.subplot(122)
plt.plot(xv,y3(xv),'r')
plt.axis([0,2,-0.5,0.5])
plt.text(1.1,-0.25,r'$f(x) = e^{-x}sin(x)-cos(x)= 0$')
plt.grid(True)
plt.axhline(0)
plt.tight_layout()
plt.show()
