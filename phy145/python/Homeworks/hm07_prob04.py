#!/usr/bin/python3

import numpy as np
from random import seed, random

def myfunc(x,y,z):
    r = np.sqrt(x*x + y*y + z*z)
    return z/r**3

def mc_integration(z,xmin,xmax,ymin,ymax,ntries):
    sum = 0.0
    for itry in range(ntries):
        x = xmin + (xmax - xmin)*random()
        y = ymin + (ymax - ymin)*random()
        sum += myfunc(x,y,z)
    result = (xmax - xmin)*(ymax - ymin) * sum/ntries
    return result

def simpson_integration(z,xmin,xmax,nx,ymin,ymax,ny):

    dx = (xmax - xmin)/nx
    dy = (ymax - ymin)/ny

    sumxy = 0
    facty = 2
    for iy in range(ny+1):     # Loop gia oloklirwsi ws pros y
        y = ymin + iy * dy
        sumx  = 0              # Arxikopoiisi tou athroismatos gia x-integration
        factx = 2              # Paragontas tou athroismatos
        for ix in range(nx+1): # Loop gia oloklirwsi ws pros x
            x = xmin + ix * dx
            if ix == 0 or ix == nx:     # prwto kai teleytaio simeio
                sumx += myfunc(x,y,z)
                continue
            if factx == 2:
                factx = 4
            else:
                factx = 2
            sumx += factx * myfunc(x,y,z)
        sumx *= dx/3          # telos tis oloklirwsis ws pros x

        if iy == 0 :            # 1o simeio 
            sumxy += sumx
            continue
        if iy == ny :         # teleytaio simeio
            sumxy += sumx
            continue
        if facty == 2 :
            facty = 4
        else:
            facty = 2
        sumxy += facty * sumx  # Neo athroisma tis oloklirwsis ws pros y
    sumxy *= dy/3              # Telos tis oloklirwsis ws pros y
    return sumxy

def simpson_integration_alternative(z,xmin,xmax,nx,ymin,ymax,ny):
    ''' Ayti einai i oloklirwsi simfwna me to paradeigma twn dialeksewn '''
    dx = (xmax - xmin)/nx
    dy = (ymax - ymin)/ny

    sum = 0
    
    for iy in range(ny+1):
        y = ymin + iy*dy
        sumx = 0
        for ix in range(0,nx-1,2):
            x = xmin + ix * dx
            sumx += myfunc(x,y,z)
            x = xmin + (ix+1) * dx
            sumx += 4*myfunc(x,y,z)
            x = xmin + (ix+2) * dx
            sumx += myfunc(x,y,z)
        sumx *= dx/3
        sumxy = sumx
        if iy == 0 or iy == ny :
            factor = 1
        elif iy%2 == 1 :
            factor = 4
        elif iy%2 == 0 :
            factor = 2
        sum += factor * sumxy
    sum *= dy/3
    return sum

def main():
    seed(123456)
    G = 6.674E-11
    xupper =   5.0
    xlower =  -5.0
    yupper =   5.0
    ylower =  -5.0
    ndivx  = 100    # Arithmos ypodiairesewn ston x-aksona
    ndivy  = 100    # Arithmos ypodiairesewn ston y-aksona
    zlower = 0.1
    zupper = 1.0
    dz     = 0.1
    mass   = 1E4
    area   = (xupper - xlower) * (yupper - ylower) # for the mc integration
    rho    = mass/area
    nMCtry = int(1E6)
    Factor = G*rho
    F_theo = 2*np.pi*Factor # H dynami einai anekartiti tis apostasis apo tin
                            # epifaneia arkei oi diastaseis tis epifaneias na
                            # einai polu megaluteres apo tin apostasi z. Gia
                            # apeiri epipedi epifaneia, i dunami einai statheri
                            # kai isi me 2*pi*rho*G
    nz = int((zupper - zlower)/dz) + 1   # Arithmos simeiwn ston z-aksona
    for iz in range(nz):
        z = zlower + iz * dz
        F_mc = mc_integration(z,xlower,xupper,ylower,yupper,nMCtry)
        Fsimp = simpson_integration(z,xlower,xupper,ndivx,ylower,yupper,ndivy)
        Fsimp_alt = simpson_integration_alternative(z,xlower,xupper,ndivx,
                                                    ylower,yupper,ndivy)
        F_mc      *= Factor
        Fsimp     *= Factor
        Fsimp_alt *= Factor
        if iz == 0: 
            print("  zpos    Force via MC    F via Simpson1   F via Simpson2      F Theory")
        print("  %4.2f   %14.8E   %14.8E   %14.8E   %14.8E" %
              (z, F_mc, Fsimp, Fsimp_alt, F_theo))
main()
