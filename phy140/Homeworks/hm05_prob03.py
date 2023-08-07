#!/usr/bin/python3
'''
To programma xreiazetai to file measurements.dat
to opoio tha prepei na dimiourgisete opws akribws
sto pinaka pou dinetai stin askisi. i.e.
Metrisi     Maza     Epimikinsi
   1          2         42.0
   2          4         48.4
   3          6         51.3
   4          8         56.3
   5         10         58.6
'''

def read_data(file2read):
    xx, yy = [], []
    inpfile = open(file2read,'r')
    for lines in inpfile:
        try:
            cnt, x, y = lines.split()
            xx += [float(x)]
            yy += [float(y)]
        except:
            continue
    inpfile.close()
    return xx, yy


def main():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    
    infilename  = 'measurements.dat'
    
    xvalues, yvalues = read_data(infilename)
    
    sum_xsq = 0.0
    sum_x   = 0.0
    sum_y   = 0.0
    sum_xy  = 0.0
    Nmeas   = len(xvalues)
    
    for i in range(Nmeas):
        sum_xsq = sum_xsq + xvalues[i]*xvalues[i]
        sum_x   = sum_x   + xvalues[i]
        sum_y   = sum_y   + yvalues[i]
        sum_xy  = sum_xy  + xvalues[i]*yvalues[i]

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
         spread = spread + (yvalues[i] - y0 - sl*xvalues[i])**2
    
    sigma_y  = np.sqrt(spread/(Nmeas-2))
    sigma_y0 = sigma_y * np.sqrt(sum_xsq/delta)
    sigma_sl = sigma_y * np.sqrt(Nmeas/delta)
    print(40*'=','\n','Results of the fit\n',40*'=')
    print(r'Slope = %6.3f +/- %6.3f'%(sl,sigma_sl))
    print(r'Intercept = %6.3f +/- %6.3f'%(y0,sigma_y0))
    print(r'Error on y = %6.3f'%sigma_y)
    print(40*'=')
    
    yerr = [sigma_y for k in range(Nmeas)]
    xv=[k*0.1 for k in range(111)]
    yfit=[sl*x+y0 for x in xv]
    plt.errorbar(xvalues,yvalues,yerr=sigma_y,marker='o',markerfacecolor='r',
                 markersize=4,markeredgecolor='r',ecolor='r',ls='none')

    plt.plot(xv,yfit,'b-')
    plt.xlabel(r'mass, m(kg)')
    plt.ylabel(r'Displacement, $\ell$ (cm)')
    plt.text(2,58,r'$y_{fit} =(%6.3f\pm%6.3f)m + (%6.3f\pm%6.3f)$'%(sl,sigma_sl,y0,sigma_y0))
    plt.hlines(58.2,1,1.9,color='blue',linestyle='solid')
    plt.xlim(0.,11.)
    plt.show()

main()
