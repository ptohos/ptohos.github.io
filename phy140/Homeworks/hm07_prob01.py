#!/usr/bin/python3

# Python Code to find approximation
# of a ordinary differential equation
# using euler method.

#=======================
# Consider a differential equation
# dy / dx =(x + y + xy)
#=======================
def func( x, y ):
	return (x + y + x * y)
#============================
# Function for euler formula
#============================
def euler( x0, y, h, x ):
        temp = 0
        xeu = []
        yeu = []
	# Iterating till the point at which we
	# need approximation
        while x0 < x :
                temp = y
                yeu +=[y]
                xeu +=[x0]
                y = y + h * func(x0, y)
                x0 = x0 + h

	# Printing approximation
        print("Approximate solution at x = ", x, " is ", "%.6f"% y)
        return xeu, yeu
#====================================
# Function for euler-cromer formula
#====================================
def euler_cromer( x0, y, h, x ):
        temp = 0
        xec = []
        yec = []
	# Iterating till the point at which we
	# need approximation
        while x0 < x :
                temp = y
                yec +=[y]
                xec +=[x0]
                y = yec[-1] + h * func(x0, y)  # Euler step to the end
                y = yec[-1] + h * func(x0+h,y) # Euler-crommer - use the deriv.
                x0 = x0 + h                # at the end of the interval 

	# Printing approximation
        print("Approximate solution at x = ", x, " is ", "%.6f"% y)
        return xec, yec
#=======================
# Driver Code
# Initial Values
import matplotlib.pyplot as plt
x0 = 0
y0 = 1
x  = 2.5
h = 0.025

# Value of x at which we need approximation
xpleu, ypleu = euler(x0, y0, h, x)
xplec, yplec = euler_cromer(x0, y0, h, x)

#
plt.figure(figsize=(6,6))
plt.plot(xpleu,ypleu,'r-')
plt.plot(xplec,yplec,'b--')
plt.xlabel('x')
plt.ylabel('y')
plt.text(0.5, 400, 'Euler')
plt.text(0.5, 350, 'Euler-Cromer')
plt.hlines(405.0,0.3,0.48,color='r',linestyle='solid')
plt.hlines(355.0,0.3,0.48,color='b',linestyle='dashed')
plt.show()
