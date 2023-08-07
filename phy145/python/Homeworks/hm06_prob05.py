#!/usr/bin/python3

''' ==================================================================
... Lusi gia to provlima ayksisis enos pluthismou ston 
... opoio periexetai enas oros meiwsis tou upsomenos sto 
... tetragwno.
... dN/dt = a*N - b*N^2
...
... H arithmitiki lusi tou provlimatos ginetai me ti methodo tou
... endiamesou simeiou
...
... H analutiki lusi tou provlimatos einai 
... N(t) = N0 * a * exp(a*t)/{a - b * N0 + b * N0 * exp(at)}
...
... To programma dexetai san parametrous eisagwgis 
...  1) To stathero oro a
...  2) To stathero oro b
...  3) Ton arxiko plithysmo N0
...  4) To xroniko vima dt
...  5) To megisto xroniko diastima tmax
...
... To apotelesma twn upologismwn dinontai sto file 'plithismos.dat'
... To executable tha prepei na to treksete 2 fores 
... gia tis 2 diaforetikes periptwseis twn timwn a kai b
...  A) Periptwsi:  A = 10, B=3, N0 = 10, dt = 0.001mines, tmax = 12mines
...  B) Periptwsi:  A = 10, B=0.01, N0 = 1000, dt=0.001mines tmax = 12mines
    ==================================================================='''
import numpy as np
import matplotlib.pyplot as plt


def theoretical(time):
    theory = N0 * afactor * np.exp(afactor * time)
    try:
        denom = afactor - bfactor * N0 + N0 * bfactor * np.exp(afactor * time)
        return theory/denom
    except:
        print('Denominator of theoretical formula is 0')
        return -1
        exit()

def d1Ndt(time,N):
    return afactor * N - bfactor * N * N

def rk4(t_i, t_f, N_i):
    '''========================================================
        Runge-Kutta 4th-order
       ========================================================
       Input arguments:
         t_i : arxiki xroniki stigmi tou diastimatos
         t_f : teliki xroniki stigmi tou diastimatos
         N_i : plithismos gia tin arxiki stigmi 
        Output variable
         N_fin: plithismos sto telos tou xronikou diastimatos
       ======================================================='''
    h = t_f - t_i
    hh = h/2
    t  = t_i

    # Ypologismos tou k1
    k1 = d1Ndt(t,N_i)                # H paragwgos stin arxi tou diastimatos
    # Ypologismos tou k2 
    k2 = d1Ndt(t+hh, N_i + k1*hh)    # H paragwgos sto meso tou diastimatos
    # Ypologismos tou k3
    k3 = d1Ndt(t+hh, N_i + k2*hh)    # H paragwgos sto meso toy diastimatos
                                     # me tin paragwgo k2
    # Ypologismos tou k4        
    k4 = d1Ndt(t+hh, N_i + k3*h)     # H paragwgos sto telos tou diastimatos
                                     # me tin paragwgo k3
    # Teliko apotelesma
    N_f = N_i + (k1 + 2*k2 + 2*k3 + k4) * h/6.
    return N_f

def main():
    global afactor, bfactor
    global tmax, N0
    tmax = float(input("Give the max time interval [tmax=10] "))
    tstep = float(input("Give the time step [tstep=0.001] "))
    t0  = float(input("Give the initial time moment [t0 = 0] "))
    afactor = float(input("Give the value of the A constant [afactor=10] "))
    bfactor = float(input("Give the value of the B constant [bfactor=3/0.01 ] "))
    N0 = int(input("Give the initial population [N(t=0)=10/1000 ] "))

    t_in = t0     # Initial moment
    N_in = N0
    theory = theoretical(t_in)
    N_RK4 = N_in
    
    Time, NPopulation = [], []
    TheoryRes = []
    
    KeepLooping = True

    while (KeepLooping):
        Time.append(t_in)
        NPopulation.append(N_RK4)
        TheoryRes.append(theory)
        
        t_fin = t_in + tstep
        N_RK4 = rk4(t_in,t_fin,N_in)
        
        #Epomeno vima
        #=============
        t_in = t_fin
        N_in = N_RK4
        theory = theoretical(t_in)
        
        #Elegxos an ftasame sti megisti epiitrepomeni stigmi
        if (t_in > tmax or theory < 0) :
            KeepLooping = False

    plt.figure(figsize=(8,5))
    plt.plot(Time, NPopulation,'ro')
    plt.plot(Time, TheoryRes,'b-')
    plt.xlabel('Time (s)', fontsize=16)
    plt.ylabel('Population',fontsize=16)
    plt.ylim(0,1.1*N0)
    plt.text(2,0.85*N0,r'$ A_{Factor} = %4.1f $'% (afactor),fontsize=15) 
    plt.text(2,0.75*N0,r'$B_{Factor} = %4.1f$' % (bfactor),fontsize=15)
    plt.text(2,0.65*N0,r'N(t=0) = %d '% (N0),fontsize=15)
    plt.text(2,0.55*N0,r'tstep = %4.3f'% (tstep),fontsize=15)
    plt.text(2,0.45*N0,r'$N(t) = \frac{ N_{0} A_{Factor} e^{A_{Factor} t} } { A_{Factor} - B_{Factor} N_{0}e^{A_{Factor}t } }$',fontsize=16)
    plt.grid(True)
    plt.show()

main()
    
