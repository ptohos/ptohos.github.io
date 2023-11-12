#!/usr/bin/python3
'''
File pendulum.dat periexei ta dedomena sti morfi
Metrisi     Mikos     Periodos
   1         0.1       1.304
   2         0.2       2.087
   3         0.3       2.354
   4         0.4       2.910
   5         0.5       3.162
   6         0.6       3.341
   7         0.7       3.647
   8         0.8       4.024
   9         0.9       4.153
  10         1.0       4.483
'''
def read_data(file2read):
    xx, yy = [], []
    inpfile = open(file2read,'r')
    for lines in inpfile:
        try:
            data = lines.strip().split()
            if data[0] == '' or len(data)<3 : continue
            xx += [float(data[1])]
            yy += [float(data[2])]
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
    y0_int = sum_xsq * sum_y - sum_x * sum_xy
    slope  = Nmeas * sum_xy - sum_x * sum_y
    try:
        slope = slope/delta
        y0_int = y0_int/delta
    except ZeroDivisionError:
         print('Determinant zero')
         print('Stoping program')
         sys.exit(1)

    spread = 0.0
    for i in range(Nmeas):
         spread = spread + (yv[i] - y0_int - slope*xv[i])**2
    sigma_y  = np.sqrt(spread/(Nmeas-2))
    sigma_y0_int = sigma_y * np.sqrt(sum_xsq/delta)
    sigma_slope  = sigma_y * np.sqrt(Nmeas/delta)

    return slope, sigma_slope, y0_int, sigma_y0_int, sigma_y 

def main():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    infilename = 'pendulum.dat'
    
    xvalues, yvalues = read_data(infilename)
    LogXval = [np.log(x) for x in xvalues]
    LogYval = [np.log(y) for y in yvalues]
    slope,sigma_sl,intercept,sigma_inter,sigma_y = naive_fit(LogXval,LogYval)
    
    plt.figure(1,figsize=(8,5))
    plt.subplot(1,2,1)
    plt.plot(xvalues,yvalues,'bp')
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.grid(True)
    #
    plt.subplot(1,2,2)
    plt.loglog(xvalues,yvalues,'bp')
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.xlim(0.07,2)
    plt.ylim(0.4,10)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Kataskeui tis eytheias
    newX = [0.1+k*0.1 for k in range(1001)]
    newY = [np.exp(intercept) * (Xnew**slope) for Xnew in newX]
    Yintercept = np.exp(intercept)
    #
    plt.figure(2,figsize=(8,5))
    plt.subplot(1,2,1)
    plt.plot(LogXval,LogYval,'bp')
    xscale = [-3+k*0.01 for k in range(351)]
    plt.plot(xscale,[intercept+slope*xv for xv in xscale],'r-',lw=2)
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.text(-2,0.3,r'$log(Y) = %3.1f + %3.1f*log(X)$'%(intercept,slope))
    plt.grid(True)
    #
    plt.subplot(1,2,2)
    plt.loglog(xvalues,yvalues,'bo')
    plt.loglog(newX,newY,'r-',lw=2)
    plt.xlabel(r'Length, $\ell$ (m)')
    plt.ylabel(r'Period, T (s)')
    plt.xlim(0.05,2.0)
    plt.ylim(0.4,10)
    plt.grid(True,which="both",ls='-')  # grid lines stis mikres upodiaireseis
    #
    plt.axvline(x=1,color='green', linestyle='--')
    plt.axhline(y=Yintercept,color='green',linestyle='--')
    xin = 1
    yin = Yintercept
    plt.plot(xin,yin,'gs')
    plt.text(1.1,4.0,'Intercept(%2.1f,%4.2f)'%(1,yin))
    plt.text(0.1,8.3,r'$y(x) = e^{intercept}*x^{slope}$')
    plt.text(0.1,7.0,r'$y(x) = %3.1f x^{%3.1f}$'%(yin,slope))  
    plt.text(0.1,6.0,r'$\sigma_y = %3.1f$'%(np.exp(sigma_y)))
    gvalue = 4*(np.pi)**2/Yintercept**2
    plt.text(0.1,5.0,r'$g = \frac{4\pi^2}{Yintercept^2} = %4.2f$'%gvalue)
    plt.tight_layout()
    plt.show()
    #
    
main()    
