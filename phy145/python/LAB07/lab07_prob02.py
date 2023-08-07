from numpy import linspace, exp, cos, pi

def f(x):
    return exp(-x**2)*cos(4*x)

nbins=int(input("Input the number of bins "))
x = linspace(0, 4, nbins)
y = f(x)

root = None  # Initialization
for i in range(len(x)-1):
    if y[i]*y[i+1] < 0:
        root = x[i] - (x[i+1] - x[i])/(y[i+1] - y[i]) * y[i]
        break  # Jump out of loop
    elif y[i] == 0:       
        root = x[i]
        break  # Jump out of loop

if root is None:
    print('Could not find any root in [%g, %g]' % (x[0], x[-1]))
else:
    print('Find (the first) root as x=%g' % root)
    print('The error is %7.3e'%abs(root-pi/8))
