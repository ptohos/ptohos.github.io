#!/usr/bin/python3

from numpy import exp, cos
def brute_force_finder(f, a, b, n):
    x = [a+x*(b-a)/n for x in range(n+1)]
    y = list(map(f,x))
    roots = []
    for i in range(1, n-1):
        if y[i+1]*y[i] < 0 :
            root = x[i] - y[i]*(x[i+1] - x[i])/(y[i+1] - y[i])
            roots.append(root)
    return roots

def f(x):
	return exp(-x**2)*cos(4*x)

def demo():
    roots = brute_force_finder(f,0,4,1001)
    if roots:
      print(roots)
    else:
      print("Could not find any roots")

if __name__ == '__main__':
    demo()
    
