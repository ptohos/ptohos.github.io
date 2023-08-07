#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

'''
==============================================================================
  To programma ayto apanta sta mporei na xrisimopoiithei gia ta 
  4 erwtimata tis askisis me ti xrisi diaforwn epilogwn:  
  I analutiki lusi eksartatai apo to platos tis talantwsis kai den 
  upologizetai
  Oi epiloges einai:
  Option 0:  erwtimata 1-4 gia dt = 0.05
  Option 1:  erwtimata 1-4 gia veltisto xroniko vima opoy Delta(amp2/amp1)<1%
  Option 2:  erwtimata 5-6 gia veltisto xroniko vima opws vrethike sto 3
==============================================================================
'''

def interpolate(x0, x1, y0, y1, x):
    ''' Grammiki paremvoli (y-y0)/(x-x0) = (y1-y0)/(x1-x0) klisi eytheias.
        To simeio (x,y) einai stin eytheia pou orizoun ta simeia (x0,y0) kai
        (x1,y1). Analoga me to zitoumeno, lynoume ws pros x or y '''

    return y0 + (y1-y0)*(x-x0)/(x1-x0)

def acceleration(k,m,xpos,vel):
    ''' Epitaxusni. Mporei na eksartatai kai apo tin taxytita ''' 
    return -(k/m)*xpos**3

def energy(k, m, xpos, vel):
    ''' Oliki mixaniki energeia tou talantwti '''
    return 0.25*m*k*xpos**4 + 0.5*m*vel*vel

def optimum_tstep(k, m, tstep_in, x0, v0, precision):
    tstep = tstep_in
    tmax  = 4*np.pi
    KeepLooping = True
    tstep_optimal  = tstep
    
    while KeepLooping:
        x = x0
        v = v0
        time = 0.0
        ampl1 = 0.0
        ampl2 = 0.0
        while time <= tmax :
            tprev = time
            xprev = x
            vprev = v
            a = acceleration(k,m,x,v)
            x += v * tstep + 0.5 * a * tstep * tstep
            v += a * tstep
            time += tstep
            
            ''' Elegxoume an i taxutita allazei prosimo. Auto 
                dilwnei oti to swma perase apo akrotato kinisis '''
            if vprev >=0 and v <= 0.0 :
                ampl = xprev
                if x > ampl:
                    ampl = x
                if ampl1 == 0:
                    ampl1 = ampl   # To prwto akrotato tis kinisis
                elif ampl2 == 0:
                    ampl2 = ampl   # To deytero akrotati
                    break          # Exoume brei ta 2 akrotata
                
        fract_change = ampl2/ampl1 - 1
        if fract_change > precision :
            tstep = tstep/2
        else:
            KeepLooping = False
            tstep_optimal = tstep
    return tstep_optimal, ampl1, ampl2

def main():
    dt_init = 0.05
    x0pos   = 0.0
    kspr    = 4.0
    mass    = 1.0
    v0      = 1.0
    vmax    = v0
    epsi    = 0.01
    KeepLooping = True
    
    SfalmaE, Energies = [],[]
    Periods, Time     = [],[]
    Xpos, Velo        = [],[]
    print("Epilexte gia ta erwtimata")
    print("Epiloges: [0:Erwtima (a), 1:Erwtima (b)-(d) 2:Erwtima (e)")
    ioption = int(input("Eisagete enan arithmo metaksu [0,1,2] "))

    if ioption < 0 or ioption > 2 :
        print("H epilogi %d den einai diathesimi"%(ioption))
        print("Epilxte ena noumero metaksu 0 kai 2")
        exit()

    if ioption >= 1 :
        print("Prosdiorismos tou veltistou xronikou vimatos dt")
        best_dt,amplit1,amplit2 = optimum_tstep(kspr,mass,dt_init,x0pos,v0,epsi)
        print("Veltisto xroniko vima einai %6.4f"%(best_dt))
        print("To 1o megisto tis kinisis = %6.4f"%(amplit1))
        print("To 2o megisto tis kinisis = %6.4f"%(amplit2))
        print("To %s allagis timwn akrotitwn = %6.4f%s"%
              (repr('%'),(amplit2/amplit1-1)*100,repr('%')))
        dt = best_dt
        
    if ioption == 2:
        Periods = []
        Energies= []
        v0   = 0.25
        vmax = 8.0

    while KeepLooping:
        time  = 0
        x     = x0pos
        xprev = x
        v     = v0
        tmax  = 4*np.pi
        Ene0  = energy(kspr,mass,x,v)
        if ioption == 0:
            dt = dt_init
        else:
            dt,amplit1,amplit2 = optimum_tstep(kspr,mass,dt_init,x0pos,v0,epsi)
            print('For velocity %4.2f m/s the best time step is %10.8f'%(v0,dt))
        
        if ioption <= 1:
            E_diff = energy(kspr,mass,x,v) - Ene0
            SfalmaE.append(E_diff)
            Xpos.append(x)
            Velo.append(v)
            Time.append(time)
            
        while (ioption <=1 and time < tmax) or (ioption == 2 and not (xprev < 0 and x>=0)):
            ''' Diatirisi twn proigoumenwn timwn gia grammiki paremvoli '''
            tprev = time
            xprev = x
            vprev = v
            a = acceleration(kspr,mass,x,v)
            x += v*dt + 0.5*a*dt*dt
            v += a*dt
            time += dt
            E_diff = energy(kspr,mass,x,v) - Ene0
            if ioption <= 1:
                SfalmaE.append(E_diff)
                Xpos.append(x)
                Velo.append(v)
                Time.append(time)
                if (time >= tmax):
                    KeepLooping = False
        if ioption == 2 :
            period = interpolate(xprev,x,tprev,time,0.)
            Periods.append(period)
            Energies.append(Ene0)
            v0 *= 2   # Diplasiasmos tis arxikis taxutitas wste na exoume 
                      # oles tis times tou erwtimatos (e)
                      # 0.25, 0.5, 1.0, 2.0, 4.0 kai 8.0
            if v0>vmax:
                KeepLooping=False
        
    if ioption <= 1:
        plt.figure(figsize=(10,6))
        plt.subplot(1,2,1)
        plt.plot(Time,Xpos,'b-')
        plt.xlabel('Time (s)')
        plt.ylabel('position x (m)')
        if ioption == 1:
            ymin = -1.1
            ymax =  1.1
            ytxt =  1.0
        else:
            ymin = -1.3
            ymax =  1.3
            ytxt =  1.1
        plt.ylim(ymin,ymax)
        plt.text(0,ytxt,f'Time step = {dt}')
        plt.text(0,ytxt-0.1,f'Velocity = {v0}m/s')
        plt.grid(True)
        #
        plt.subplot(1,2,2)
        plt.plot(Velo,Xpos,'r-')
        plt.xlabel('Velocity u (m/s)')
        plt.ylabel('position x (m)')
        plt.xlim(-1.75,1.75)
        plt.ylim(ymin,ymax)
        plt.text(-1.5,ytxt,f'Time step = {dt}')
        plt.text(0.5,-0.1,f'Velocity = {v0}m/s')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        #
        if ioption == 1:
            plt.figure(figsize=(7,5))
            plt.plot(Time,SfalmaE,'b-')
            plt.xlabel('Time (s)')
            plt.ylabel(r'$\Delta E$ (J)')
            plt.grid(True)
            plt.show()
    if ioption == 2:
        plt.figure(figsize=(7,5))
        plt.plot(Energies,Periods,'b-')
        plt.xlabel('Energy (J)')
        plt.ylabel('Period (s)')
        plt.grid(True)
        plt.show()
        
main()
