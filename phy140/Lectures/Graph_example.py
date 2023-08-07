import numpy as np
import matplotlib.pyplot as plt
#
def func1(x):
   return 4*np.exp(-2*x)
def func2(x):
   return 0.5*x**2
def func_diff(x):
   return 4*np.exp(-2*x)-0.5*x**2
#
x=[x*0.01 for x in range(0,201)]   # Times apo 0 ews 2 me vima 0.01 
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,list(map(func1,x)),'r-')
plt.plot(x,list(map(func2,x)),'b--')
plt.text(0.4,2.0,r'f(x)=$4e^{-2x}$')
plt.text(1.5,1.0,r'f(x) = $0.5x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(x,list(map(func_diff,x)),'b-')
plt.text(0.5,1.5,r'f(x) = $4e^{-2x} - 0.5x{^2}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True) 
plt.axhline(y=0,color='red',linestyle='--') 
plt.tight_layout() 
plt.show()
