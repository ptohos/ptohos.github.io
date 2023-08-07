import numpy as np
import matplotlib.pyplot as plt

# read data from file
xdata,ydata = np.loadtxt("lab13_prob01.dat",unpack=True)

#Dimiourgia x kai y arrays gia to grafima tis sunartisis
x=np.linspace(-10.,10.,200)
y = np.sin(x) * np.exp(-(x/5.0)**2)

#Dimiourgia grafimatos
plt.figure(1,figsize=(8,6))              # figsize dinei to megethos toy canvas
plt.plot(x,y,'g-',label='theory')        # prasini sunexis grammi 
plt.plot(xdata,ydata, 'bo', label="data")    # 'bo' blue circles
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right', title = 'legend')
plt.axhline(color='gray',zorder=-1)
plt.axvline(color='gray',zorder=-1)
#
plt.savefig('prob13_1b.pdf')
#
plt.show()
