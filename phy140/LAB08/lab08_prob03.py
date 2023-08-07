from numpy import exp, cos, pi
import matplotlib.pyplot as plt

def f(x):
    return exp(-x**2)*cos(4*x)

nbins=int(input("Input the number of bins "))

xmin = 0
xmax = 4
dx = (xmax - xmin)/nbins
x = [xmin+dx*i for i in range(nbins+1)]
y = list(map(f,x))

root = None  # Initialization
for i in range(len(x)-1):
    if y[i]*y[i+1] < 0:
        # grammiki paremvoli
        root = x[i] - (x[i+1] - x[i])/(y[i+1] - y[i]) * y[i]
        break  # Jump out of loop
    elif y[i] == 0:       
        root = x[i]
        break  # Jump out of loop

if root is None:
    print('Could not find any root in [%g, %g]' % (x[0], x[-1]))
else:
    print('Find (the first) root as x=%g' % root)
    print('The error is %7.3e for %d steps'%(abs(root-pi/8),nbins))

plt.figure(figsize=(6,4))
plt.plot(x,y,'b-')
plt.grid(True)
plt.xlabel('x')
plt.ylabel(r'f(x) = $e^{-x^2}cos(4x)$')
plt.xlim(0.,4.)
plt.ylim(-0.6,1.01)
plt.show()
