#!/usr/bon/python03

import numpy as np
import matplotlib.pyplot as plt



def ReadTheData(inpfilename):
    inpfile = open(inpfilename,'r')
    xx = []
    yy = []
    for line in inpfile:
        ''' strip() ti grammi apo kena deksia kai aristera
            kai anagnwsi me twn dedomenwn me kena metaksu tous'''
        imeas, x, y = line.strip().split()
        ''' Elexgos an i proti leksi den exei psifia - Xrisi loop comprehension
            gia kathe xaraktira mesa sti leksi kai tis methodous isdigit()'''
        if not any( char.isdigit() for char in imeas ): continue
        xx += [float(x)]
        yy += [float(y)]
    inpfile.close()
    return xx, yy

#========
# Main
#========
filename = input("Give the name of the data file ")
filename2 = input("Give the output filename ")

mass, length = ReadTheData(filename) 

Nmeas   = len(mass)
sum_xsq = 0
sum_x   = 0
sum_y   = 0
sum_xy  = 0
for i in range(Nmeas):
    sum_xsq += mass[i]*mass[i]
    sum_x   += mass[i]
    sum_y   += length[i]
    sum_xy  += mass[i]*length[i]
delta = Nmeas * sum_xsq - sum_x * sum_x
y0    = sum_xsq * sum_y - sum_x * sum_xy
slope = Nmeas * sum_xy - sum_x * sum_y
if delta != 0:
    slope /= delta
    y0    /= delta
else:
    print("Determinant zero")
    print("Stop execution")
    exit()

spread = 0
for i in range(Nmeas):
    spread += (length[i] - y0 - slope*mass[i])*(length[i] - y0 - slope*mass[i])
sigma_y     = np.sqrt(spread/(Nmeas-2))
sigma_y0    = sigma_y * np.sqrt(sum_xsq/delta)
sigma_slope = sigma_y * np.sqrt(Nmeas/delta)

print(40*('='),'\n  %35s'%'Resuls of the fit',
      '\n Slope = %14.3f +/- %6.3f'%(slope,sigma_slope),
      '\n Intercept = %10.3f +/- %6.3f'%(y0, sigma_y0),
      '\n Sfalma sto y = %6.3f\n'%sigma_y, 40*('='))

outfile = open(filename2,'w')
ytheory = []
yerror  = []
for i in range(Nmeas):
    ytheory += [y0 + slope * mass[i]]
    yerror  += [sigma_y]
    outfile.write(' %7.4f  %7.4f  %7.4f  %7.4f' %
                  (mass[i], length[i], yerror[i], ytheory[i]))
outfile.close()
masf=[]
leng=[]
masf += [0]
masf += [mass[0]]
leng += [y0]
leng += [ytheory[0]]
plt.figure(figsize=(8,4))
plt.errorbar(mass,length,fmt='oC1',label='data',yerr=yerror,ecolor='black')
plt.plot(mass,ytheory,'C0-',label='fit')
plt.plot(masf,leng,'C0--')
plt.title('Least square fit results')
plt.xlabel('Mass (kg)')
plt.ylabel('Length (cm)')
plt.xlim(0,12)
plt.ylim(35,60)
plt.text(1,57,fr'$\ell$ = ({y0:5.2f} $\pm$ {sigma_y0:4.2f}) + ({slope:4.2f} $\pm$ {sigma_slope: 4.2f})mass')
plt.legend()
plt.savefig('FitMeasurements.pdf')
plt.show()

