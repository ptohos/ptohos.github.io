import numpy as np
import matplotlib.pyplot as plt
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
plt.figure(num=None,figsize=(12,6),dpi=80,facecolor='w',edgecolor='k')
plt.subplot(121)
plt.plot(x,y2,x,y3)
plt.grid(True)
plt.axis([-2,4,-5,20])
plt.text(-1,8,r'$f1(x)=5.0+4x$')
plt.text(1.5,18,r'$f2(x)=e^x$')
plt.subplot(122)
plt.plot(x,y1,'r')
plt.axis([-6,4,-3,9])
plt.text(0,7,r'$f(x) = 5+4x-e^x = 0$')
plt.grid(True)
plt.axhline(0)
plt.show()
