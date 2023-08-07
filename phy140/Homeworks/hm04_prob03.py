#!/usr/bin/python3

import matplotlib.pyplot as plt

def findmax(x, y):
    maxima = []
    for k in range(1, len(y)-1, 1):
        if y[k-1] < y[k] > y[k+1]:
            maxima.append((x[k], y[k]))
    # Distances between maxima:
    dist = []
    for k in range(len(maxima)-1):
        dist.append(maxima[k+1][0] - maxima[k][0])
    
    return maxima, dist

from numpy import cos, pi, exp
# Use a simple curve where we know the maxima
# (here all integer x) and distances (here 1)
def f(x):
    return exp(-0.1*x)*cos(2*pi*x)

x = [i/10 for i in range(101)]   # 101 points me apostasi 0.01 sto [0,10]
y = list(map(f,x))

maxima, dist = findmax(x,y)
ymaxima = []; xmaxima = []
for j in range(len(maxima)):     # Eyresi tou arithmou twn grammwn
   ymaxima += [ maxima[j][1] ]   # Apothikeusi twn stoixeiwn tis 2-is stilis 
   xmaxima += [ maxima[j][0] ]
ymaxima_max = max(ymaxima)
ymaxima_min = min(ymaxima)
print("Maximum is at %.4f and the minimum at %.4f"%(ymaxima_max,ymaxima_min))
plt.plot(x,y)
plt.show()

plt.plot(xmaxima,ymaxima)
plt.show()
