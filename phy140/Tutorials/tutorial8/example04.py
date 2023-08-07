#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Example usage of symbolic calculations

Prerequisites:
sudo pip install --upgrade pip
sudo pip install sympy

Links:
https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html
https://docs.sympy.org/dev/modules/utilities/lambdify.html
'''
import sympy as s
import matplotlib.pyplot as plt

x   = s.Symbol("x")
y   = s.Symbol("y")
f   = x**6 + 2*x**3 + x*2 + x - 4
intF= s.integrate(f, x)
df  = s.diff(f, x)
ddf = s.diff(df, x)
print("f = ", f)
print("intF = ", intF)
print("df = ", df)
print("ddf = ", ddf)
print("integrate(df, x) = ", s.integrate(df, x))

xList   = [i for i in range(0, 100)]
F       = s.lambdify(x, f)
INTF    = s.lambdify(x, intF)
DF      = s.lambdify(x, df)
DDF     = s.lambdify(x, ddf)
fList   = [F(x) for x in xList]
intList = [INTF(x) for x in xList]
dfList  = [DF(x) for x in xList]
ddfList = [DDF(x) for x in xList]

# Create the canvas
plt.figure(figsize=(14,7))
plt.subplot(1,1,1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(xList, fList   , 'bo', label=r'$f(x)$')
plt.plot(xList, intList , 'ko', label=r'$\int f(x) {dx}$')
plt.plot(xList, dfList  , 'ro', label=r'$\frac{df}{dx}$')
plt.plot(xList, ddfList , 'go', label=r'$\frac{d^{2}f}{dx^{2}}$')
plt.legend(title="")
plt.grid(True)
plt.show()

print("=== Done!")
quit()
