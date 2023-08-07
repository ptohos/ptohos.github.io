#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Example usage of matplotlib pyplot library

Links:
https://matplotlib.org/2.2.5/api/_as_gen/matplotlib.pyplot.colors.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
https://www.color-hex.com
https://www.askpython.com/python/examples/mean-and-standard-deviation-python
'''
import numpy as np
import matplotlib.pyplot as plt
import random as rndm

def myGauss(x, mu, sigma):
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*( (x-mu)/sigma)**2)

def getMean(content, binvalues):
    '''
    Lecture 7, page 31:
    Sum_{i}^{all bins} x_{i} F_{i} = x_{i} * (f_{i} * dx_{i})
    
    where: 
    
    f_{i} = F_{i}/dx_{i}     [prob. density]
    F_{i} = f_{i} * dx_{i}   [frequency]

    '''
    nBins = len(binvalues)
    dx    = binvalues[1]-binvalues[0] # constant
    xMid  = [0.5*(binvalues[1]+binvalues[i-1]) for i in range(1, len(binvalues))]
    mean  = 0.0
    
    for i in range(nBins-1):
        f = content[i]
        x = xMid[i]
        mean += x * (f * dx)
    return mean

def getIntegral(fList, dx):
    '''
    Lecture 7, page 25:
    Sum_{i}^{all bins} f_{i} dx_{i}
    '''
    integral = 0.0
    for f in fList:
        integral += f * dx
    return integral

def getStDev(data):
    '''
    Easier to use the sum() built-in python function!
    '''
    var = getVariance(data)
    std_dev = np.sqrt(var)
    return std_dev

def getVariance(data):
    '''
    Easier to use the sum() built-in python function
    with list comprehension.
    '''
    N = len(data)
    mean = sum(data) / N
    return sum((x - mean) ** 2 for x in data) / (N)

if 1:
    N, mean, sigma = input("Enter histogram population and Gaussian parameters (N,mean,standDev) :").strip().split(",")
    N = int(N)
    mean = float(mean)
    sigma = float(sigma)
else:
    N = 1000
    mean  = 20
    sigma = 5

# Variable definition
xMin = mean-5*sigma
xMax = mean+5*sigma
kBrazilGold  = "#f8e31c"
kBrazilGreen = "#1d9e3a"
kBrazilBlue  = "#161f75"

# Create N histogram entries
h = []
for i in range(N+1):
    h.append( rndm.gauss(mean, sigma))
    
# Create the canvas
plt.figure()

# Create histogram (content = freq. density, binvalues= x-values in the defined intervals, list of intermediate calculations)
content, binvalues, interm=plt.hist(h, bins=50, density=True, facecolor=kBrazilBlue, alpha=0.5, histtype='bar', label="N = %d" % (N) )

# Create the Gaussian function
x = np.arange(xMin, xMax, 1/100)
y = [myGauss(v, mean, sigma) for v in x]

xOneSigma = np.arange(mean-1*sigma, mean+1*sigma, 1/100)
yOneSigma = [myGauss(x, mean, sigma) for x in xOneSigma] #list(map(myGauss, xOneSigma))

xTwoSigma = np.arange(mean-2*sigma, mean+2*sigma, 1/100)
yTwoSigma = [myGauss(x, mean, sigma) for x in xTwoSigma] #list(map(myGauss, xTwoSigma))

# Enable the grid?
plt.grid(False)

# Draw the plot on the canvas
plt.plot(x, y, kBrazilBlue, lw=3, alpha=0.5, label=r'$\mu=%.1f$, $\sigma=%.1f$' % (mean, sigma) )

# Add information on canvas (labels, title)
plt.title("Guassian Distribution", size=12, weight='bold')
plt.xlabel("x")
plt.ylabel("probability density function (PDF)")

# Fill the area behind the curve
plt.fill_between(x, y, 0, alpha=1.0, color='w')
plt.fill_between(xTwoSigma  , yTwoSigma  , 0, alpha=0.9, color=kBrazilGold, label=r'1$\sigma$ = 68%')
plt.fill_between(xOneSigma  , yOneSigma  , 0, alpha=0.9, color=kBrazilGreen, label=r'2$\sigma$ = 95%')

# Add error bars? find the mid-points of the bins and add them
xMid = [0.5*(binvalues[i-1]+binvalues[i]) for i in range(1, len(binvalues))]
xErr = 0.5*(binvalues[1]-binvalues[0])
yErr = [c/np.sqrt(N) for c in content]
plt.errorbar(xMid, content, yerr=yErr, xerr=xErr, fmt='none', color=kBrazilBlue)

# Add legend to plot
plt.legend(title="Parameters: ")

# Add line at x=mean?
plt.axvline(mean, color='black', linestyle="--", lw=1)


# Calculate integral, mean, variance, standard deviation
dx = binvalues[1]-binvalues[0]
integral = getIntegral(content, dx)
mean     = getMean(content, binvalues)
variance = getVariance(h)
stdDev   = getStDev(h)
print("===Histogram calculations:" )
print("\tintegral = %.2f" % (integral))
print("\tmean = %.2f" % (mean))
print("\tvar = %.2f" % (variance))
print("\tstdDev = %.2f" % (stdDev))


if 0:
    plt.show()
else:
    plt.savefig("example01_N%s_Mean%s_Sigma%s.pdf" % (N, str(mean).replace(".", "p"), str(sigma).replace(".", "p")) )

quit()


