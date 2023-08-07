#!/usr/bin/python3

'''==================================================
     To programma ayto briskei to magnitiko pedio 
     pou dimiourgeitai apo ena eythugrammo agwgo 
     pou diarreetai apo reuma I xrisimopoiwntas 
     ti methodo oloklirwsis Simpson. 
     B = mu*)/(4*pi) * [dz*sin(theta)]/r^2 kai sin(theta)=x/r
     B = mu*I/(4*pi) * (x*dz)/(z^2+x^2)^(3/2) 
     H ologklirwsi symfvna me ti methodo Simpson dinei:
     B + muo*I*x*dz/[3*(4*pi)] * [f(-L/2)+4*f(-L/2+dz)+2f(-L/2+2*dz)+...+f(L/2)}
   ==================================================
'''
import numpy as np
import matplotlib.pyplot as plt

def Simpson(myfunc,xloc, zdiv, lowLim, uppLim):
    dz = (uppLim - lowLim)/zdiv
    result = 0
    for iz in range(0, zdiv - 1, 2):
        za = lowLim + iz*dz
        zb = lowLim + (iz+1)*dz
        zc = lowLim + (iz+2)*dz
        result += myfunc(xloc,za) + 4*myfunc(xloc,zb) + myfunc(xloc,zc)
    result *= dz/3
    return result

def calculate_field(xloc, length, dz):
   '''
   Ypologismos tou magnitikou pediou gia sygkekrimeni apoostasi 
   sti x-dieythunshi kai gia dz kata mikos toy agwgou
   H methodos efarmozei to athroisma Sum(dz*x/r^3), opou
   r = sqrt(x^2+z_i^2) kai z_i to meso kapoioy ypodiastimatos 
   kata mikos toy agwgou.
   To magnhtiko pedio einai stin y-dieythunsi
   '''
   Bf = 0.0
   z = -length/2
   while z <= length/2 :
       r = np.sqrt(xloc**2 + z**2)
       Bf += dz * xloc/r**3
       z  += dz
   return Bf
        
def myfunc(xpos,zpos):
    distsq = np.sqrt(zpos**2 + xpos**2)
    return xpos/(distsq)**3

def main():
    Xpos, BFSimpson, BFApprox, BFTheory = [],[],[],[]
    nxgrid = int(input("Give the number of points along x-axis [nxgrid=5000] "))
    length = float(input("Give the length of the conductor [length=1m] "))
    epsi   = float(input("Give the desired accuracy [epsi=1E-10] "))
    
    zmin = -length/2             # Ta oria oloklisrwsis ws
    zmax = length/2              # pros to mikos tou agwgou
    for ix in range(nxgrid):
        '''Xwrismos tou surmatos me to 0 sto meso'''
        IntegralBefore = 0.
        x = (ix+1)/(nxgrid)      # syntetagmeni sto x-aksona theorontas oti xmax = 1.
        ndiv = 2                 # Ksekinoume ti methodo me 2 upodiastimata
        diff = 1.0
        while diff > epsi :      # Epanaliptiki diadikasia ayksisis tou arithmou
            dz = length/ndiv     # Eyros diastimatos
            Integral = Simpson(myfunc,x,ndiv,zmin,zmax)
            diff = abs(IntegralBefore - Integral)/Integral
            IntegralBefore = Integral
            ndiv *= 2          # diplasiasmos
        Xpos.append(x)
        BFSimpson.append(Integral)
        ''' H proseggistiki methodos upologismou gia to 
            veltisto dz pou vrethike apo ti methodo Simpson
        '''
        Bvalue = calculate_field(x,length,dz)
        BFApprox.append(Bvalue)
        '''Theoritikos ypologismos apo to nomo tou Ampere
           To pedio enos reumatoforou agwgou pou diareetai apo reuma I
           isoutai me B = μοΙ/(2πr) opou r i mikroteri apostasi ston agwgo
           kai ara x gia tin periptwsi tou provlimatos
        '''
        BFTheory.append(2/x)     # To 2 prokuptei sykrinontas me ton oro μ0Ι/4π
                                 # apo to nomo Biot-Savard
    print("\tXposition\tBFSimpson\tBF_Approximate\tBF_Ampere")
    for j in range(len(BFTheory)):
        print("\t %7.4f \t %7.2f \t %7.2f \t %7.2f" % (Xpos[j],BFSimpson[j],BFApprox[j],BFTheory[j]))
    plt.figure(figsize=(7,5))
    plt.plot(Xpos,BFSimpson,'b-')
    plt.xlabel('xpos')
    plt.ylabel('Bfield')
    plt.grid(True)
    plt.show()
main()
