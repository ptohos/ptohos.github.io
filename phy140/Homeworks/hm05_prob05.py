#!/usr/bin/python3
'''
File pendulum.dat periexei ta dedomena sti morfi
 L    T
0.1  0.6
0.2  0.9
0.3  1.1
0.4  1.3
0.5  1.4
0.6  1.6
0.7  1.7
0.8  1.8
0.9  1.9
1.0  2.0
'''
def read_data(file2read):
    xx, yy = [], []
    inpfile = open(file2read,'r')
    for lines in inpfile:
        try:
            x, y = lines.split()
            xx += [float(x)]
            yy += [float(y)]
        except:
            continue
    inpfile.close()
    return xx, yy

def naive_fit(xv,yv):
    ''' The naive fit model
    described on problem 3
    '''
    import sys
    import numpy as np
    sum_xsq = 0.0
    sum_x  = 0.0
    sum_y  = 0.0
    sum_xy = 0.0
    Nmeas  = len(xv)
    for i in range(Nmeas):
        sum_x = sum_x + xv[i]
        sum_y = sum_y + yv[i]
        sum_xy= sum_xy + xv[i]*yv[i]
        sum_xsq = sum_xsq + xv[i]*xv[i]
        
    delta = Nmeas*sum_xsq - sum_x * sum_x
    y0    = sum_xsq * sum_y - sum_x * sum_xy
    sl    = Nmeas * sum_xy - sum_x * sum_y
    try:
        sl = sl/delta
        y0 = y0/delta
    except ZeroDivisionError:
         print('Determinant zero')
         print('Stoping program')
         sys.exit(1)

    spread = 0.0
    for i in range(Nmeas):
         spread = spread + (yv[i] - y0 - sl*xv[i])**2
    sigma_y  = np.sqrt(spread/(Nmeas-2))
    sigma_y0 = sigma_y * np.sqrt(sum_xsq/delta)
    sigma_sl = sigma_y * np.sqrt(Nmeas/delta)

    return sl, sigma_sl, y0, sigma_y0, sigma_y 

def main():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    infilename  = 'pendulum.dat'
    
    xvalues, yvalues = read_data(infilename)
    LogXval = [np.log(x) for x in xvalues]
    LogYval = [np.log(y) for y in yvalues]
    
    slope,sigma_sl,intercept,sigma_inter,sigma_y = naive_fit(LogXval,LogYval)
    # Kataskeui tis eytheias
    newX = [0.1+k*0.1 for k in range(1001)]
    newY = [np.exp(intercept) * (Xnew**slope) for Xnew in newX]
    Yintercept = np.exp(intercept)
    #
    plt.figure(figsize=(8,5))
    plt.subplot(1,2,1)
    plt.plot(xvalues,yvalues,'bp')
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.grid(True)
    #
    plt.subplot(1,2,2)
    plt.loglog(xvalues,yvalues,'bo')
    plt.loglog(newX,newY,'r-',lw=2)
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.xlim(0.07,15)
    plt.ylim(0.4,4)
    plt.grid(True)
    #
    plt.axvline(x=1,color='green', linestyle='--')
    plt.axhline(y=Yintercept,color='green',linestyle='--')
    xin = 1
    yin = Yintercept
    plt.plot(xin,yin,'gs')
    plt.text(1.1,1.7,'Intercept(%2.1f,%4.2f)'%(1,yin))
    plt.text(0.1,2.8,r'$Y(X) = e^{intercept}*x^{slope}$')
    plt.text(0.1,2.5,r'$Y(X) = %3.1f X^{%3.1f}$'%(yin,slope))
    plt.tight_layout()
    plt.show()
    #
    
main()    
