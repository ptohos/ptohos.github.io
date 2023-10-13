#!/usr/bin/python3

import numpy as np
import urllib.request

def histo(data,xmin,xmax,dx):
    for i in range(len(data)):
        if data[i] > xmax: data[i]=xmax
        if data[i] < xmin: data[i]=xmin
    nbins = int((xmax-xmin)/dx)
    if nbins*dx < xmax:
        nbins = nbins+1     
    xmax = xmin+nbins*dx
    freq = np.zeros(nbins)
    xaxis = np.arange(xmin+dx/2,xmax-dx/2,dx)
    # Diastima pou anikei kathe metrisi
    for i in range(len(data)):
        ibin = int((data[i]-xmin)/dx)
        freq[ibin] = freq[ibin] + 1      
    return xaxis,freq

def get_stat(xvalues,yvalues):
    nva = 0
    sum = 0.0
    sumsq = 0.0
    for ik in yvalues:
        nva += ik
    for iv in range(len(xvalues)):
        sum   += (xvalues[iv]*yvalues[iv])
    x_aver = sum/nva
    for iv in range(len(xvalues)):
        sumsq += yvalues[iv]*(xvalues[iv]-x_aver)**2
    stdev = np.sqrt(sumsq/(nva-1))
    return x_aver, stdev

    

#==================================
#Read the data 
#==================================
web_file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/sound.dat")
MyData = np.loadtxt(web_file)
print(MyData)
print(np.average(MyData))
print(np.std(MyData))
#==================================
#Calculate the frequency and xaxis
#==================================
xaxis1,freq1 = histo(MyData,0.20,0.85,0.05)
np.savetxt('sound_out1.dat',list(zip(xaxis1,freq1)),fmt='%.3f  %4d')

xaxis2,freq2 = histo(MyData,0.20,0.85,0.1)
np.savetxt('sound_out2.dat',list(zip(xaxis2,freq2)),fmt='%.3f  %4d')

#================================
# Statistiki analysi
#================================
time_aver1, time_std1 = get_stat(xaxis1,freq1)
time_aver2, time_std2 = get_stat(xaxis2,freq2)
print('Mean time for dt = 0.05s is : %.3f +/- %.3f'%(time_aver1,time_std1))
print('Mean time for dt = 0.1s is : %.3f +/- %.3f'%(time_aver2,time_std2))
