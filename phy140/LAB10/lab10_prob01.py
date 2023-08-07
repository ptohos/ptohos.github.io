#!/usr/bin/python3
'''
Lysi tis diaforikis eksiswsis 
  y' = y => dy/y=dx=> ln(y) = x =>
  => y_theory = e^x 

'''
import numpy as np
import matplotlib.pyplot as plt


# Orismos tis sunartisis deriv gia tin paragwgo
def deriv(y):
    return y

# Orismos tis sunartisis Euler gia to vima Euler

def Euler(y,dx):
    dydx = deriv(y)      #klisi tis sunartisis tis paragwgou
    y = y + dydx * dx    # To neo y brisketai an prosthesw sto proigoumeno 
    return y             # y ti diafora poy prokuptei apo to dydx*dx

# Main program
xvalues = []
yvalues = []
ytheory = []
x_max = 2
x0 = 0.0       # Arxikes sunthikes
y0 = 1.0       # gia x kai y

fig = plt.figure();
dxstp= [0.001, 0.01, 0.1]
legd = ['dx=0.001','dx=0.01','dx=0.10']
comm = ['b--',     'm--',     'g-']
for i in range(len(legd)):
    xstep = dxstp[i]        # to megethos tou vimatos 
    xtemp = x0              # copy twn arxikwn sunthikwn gia kathe vima pou tha
    ytemp = y0              # dokimasoume se temp metavlites gia ton algorithmo
    while xtemp <= x_max :
        if i == 0 :
            ytheory.append(np.exp(xtemp))  # theoritiki timi
        xvalues.append(xtemp)
        yvalues.append(ytemp)
        ytemp = Euler(ytemp,xstep)
        xtemp = xtemp + xstep
        
    if i == 0 :
        plt.plot(xvalues,ytheory,'r-',label=r"Theoretical: $y=e^x$")
        plt.plot(xvalues,yvalues,comm[i],label=legd[i])
    else:
        plt.plot(xvalues,yvalues,comm[i],label=legd[i])

    del xvalues              # Svisimo twn pinakwn xvalues kai yvalues 
    del yvalues              # gia na xrisimopoiithoun sto epomeno vima
    xvalues,yvalues = [],[] 
    
plt.title(r"Solution to the differential equation: $\frac{dy}{dx} = y$",
          size=16)
plt.xlabel("x-values")
plt.ylabel("y-values")

plt.legend()
plt.show()

