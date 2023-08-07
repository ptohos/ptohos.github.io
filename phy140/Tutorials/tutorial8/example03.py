#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Example usage of log-log caclulations

Links:
'''
import numpy as np
import matplotlib.pyplot as plt

def getIntercept(x, y, m, logx=False, logy=False):
    '''
    Using y=mx + c, then if a point (x,y) is known and the gradient (m) is also known
    then we can evaluate the unknwon c
    '''
    if logx:
        x = np.log(x)
    if logy:
        y = np.log(y)
    return y-m*x

def getGradient(x1, x2, y1, y2, logx=False, logy=False):
    if logx:
        dx = np.log(x2) - np.log(x1)
    else:
        dx = x2-x1

    if logy:
        dy = np.log(y2) - np.log(y1)
    else:
        dy = y2-y1

    try:
        return dy/dx
    except:
        print("Problem with evaluating gradient (dx = %s, dy = %s)" % (dx, dy))
        
    
print("=== Step 1) Read the values from the file")
filename = 'lab07_motion.dat'
infile = open(filename,'r')
print("\tOpening file '%s'" % (filename) )
X, Y = [], []
for line in infile:
    try:
        x,y = line.strip().split()
        X +=[float(x)]
        Y +=[float(y)]
    except:
        print("\tProblem with line:",line)
        continue
print("\tClosing file '%s'" % (filename) )
infile.close()

print("=== Step 2) Plot the x and y values")
print("\tCreating canvas")
plt.figure(figsize=(14,7))
plt.subplot(1,3,1)
plt.xlabel('t (s)')
plt.ylabel('x (m)')
print("\tPlotting values (linear scale)")
plt.plot(X, Y, 'bo')
plt.grid(True)

plt.subplot(1,3,2)
print("\tPlotting values (log-log scale)")
plt.loglog(X, Y, 'bo')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.xlim(0.1,100)
plt.ylim(0.1,10000)
plt.grid(True)


print("=== Step 3) Determine the parameters (m, c) of the line y = mx + c:")
slope = getGradient(X[0], X[-1], Y[0], Y[-1], logx=True, logy=True)  # lambda
logA = getIntercept(X[1], Y[1], slope, logx=True, logy=True)        # log(A)
print("\tslope=%s, intercept=%s" % (slope, logA))


print("=== Step 4) Construct the graph of the line:") 
newX = np.arange(0.1,100.1,0.1)
# log(y) = log(A) + l*log(x) = log(A)*log(x)**lamda
# ==> log(y) = log(A)*log(x)**lambda    where: A=intercept, log(x)=newX, lambda=slope
A = np.exp(logA)
newY = A * newX **(slope)
Yintercept = A
print('\tThe intercept is :',Yintercept)
'''
   log(y) = log(A) + m*log(x)
=> log(y) - log(A) = m*log(x) = log(x)^{m}
=> log(y/A) = log(x^{m})
=> y/A = x^klisi
=> y = A * x^klisi

Dimiourgoume ton ajona x kai katopin tha prepei na
paroume to y = e^[intercept+klisi*log(x)].
H timi tis tetagmenis (intercept) einai: y0 = exp(intercept)
kai sumbainei gia log(X)=0 diladi X=1
'''

print("=== Step 5) Construct the new linear line")
plt.subplot(1,3,3)
plt.loglog(X,Y,'bo', label="data")
plt.loglog(newX, newY,'b-', alpha=0.6, lw=2, label=r'$x(t)=%.1f t^{%.1f}$'%(A, slope))
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.xlim(0.1,100)
plt.ylim(0.1,10000)
print("\tAdding line at x=1")
plt.axvline(x=1, color='green',linestyle='--')
print("\tAdding line at (x,y) = (1, A)")
plt.axhline(y=Yintercept,color='green',linestyle='--')
xin=1
yin=Yintercept
plt.plot(xin,yin,'gs', label='Intercept(%.1f, %.2f)'%(1,yin))
#plt.text(1.3,0.25,'Intercept(%2.1f,%4.2f)'%(1,yin))
#plt.text(10,30,r'$Y(X)=e^{intercept}*x^{slope}$')
plt.grid(True)

# Correct padding around the figures
plt.tight_layout()
plt.legend(title="")
plt.show()
print("=== Done!")
quit()
