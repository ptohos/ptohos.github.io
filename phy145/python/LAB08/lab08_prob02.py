#!/usr/bin/python3
'''
Lysi tis diaforikis eksiswsis 
  y' = y^2 + 1 => dy/(y^2+1)=dx
  opote arc(tan(y)) = x =>
   y_theory = tan(x)

Mporeite na treksete to programma dinontas
arxiko step size:  0.05
arithmo diaforetikwn vimatwn: 4   epomenws (dx=0.05, 0.10, 0.15, 0.20)
'''
import numpy as np
import matplotlib.pyplot as plt


# Orismos tis sunartisis deriv gia tin paragwgo
def deriv(y):
    return y*y + 1

# Orismos tis sunartisis Euler gia to vima Euler

def Euler(y,dx):
    dydx = deriv(y)      #klisi tis sunartisis tis paragwgou
    y = y + dydx * dx    # To neo y brisketai an prosthesw sto proigoumeno 
    return y             # y ti diafora poy prokuptei apo to dydx*dx

# Main program
dx = float(input("Give the step size for x "))
ntries = int(input("How many different steps to try? "))

xvalues = []
yvalues = []
ytheory = []
x_max = 1
x0 = 0.0       # Arxikes sunthikes
y0 = 0.0       # gia x kai y

fig = plt.figure();
legd = ['dx=0.05','dx=0.10','dx=0.15','dx=0.20']
comm = ['b--',     'm--',     'g-',   'k--']
for i in range(ntries):
    xstep = (i+1)*dx        # to megethos tou vimatos 
    xtemp = x0              # copy twn arxikwn sunthikwn gia kathe vima pou tha
    ytemp = y0              # dokimasoume se temp metavlites gia ton algorithmo
    while xtemp <= x_max :
        if i == 0 :
            ytheory.append(np.tan(xtemp))  # theoritiki timi
        xvalues.append(xtemp)
        yvalues.append(ytemp)
        ytemp = Euler(ytemp,xstep)
        xtemp = xtemp + xstep
        
    if i == 0 :
        plt.plot(xvalues,ytheory,'r-',label=r"Theoretical: $y=tan(x)$")
        plt.plot(xvalues,yvalues,comm[i],label=legd[i])
    else:
        plt.plot(xvalues,yvalues,comm[i],label=legd[i])

    del xvalues              # Svisimo twn pinakwn xvalues kai yvalues 
    del yvalues              # gia na xrisimopoiithoun sto epomeno vima
    xvalues,yvalues = [],[] 
    
plt.title(r"Solution to the differential equation: $\frac{dy}{dx} = y^2+1$",
          size=16)
plt.xlabel("x-values")
plt.ylabel("y-values")

plt.legend()
plt.show()

