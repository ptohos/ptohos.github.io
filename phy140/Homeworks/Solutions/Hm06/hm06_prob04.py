#!/usr/bin/python3

'''
 Lusi tou provlimatos tis kinisis enos 
 swmatos mesa se ygro.
 Gia tin lusi tha xrisimopoieithoun oi 
 methodoi Euler kai Euler-Cromer 
 gia ti lusi kanonikwn diaforikwn eksiswsewn

 Swma to opoio kineitai mesa se ygro, dexetai mia
 antistasi apo to ugro. H antistasti ayti einai 
 analogi ti taxutitas tou swmatos, opws prokuptei 
 an doume tis monades metrisis tis statheras b. 
 H dynami tis antistasis apo to reysto einai:
    F=-bu   (1)
 To swma kineitai ypo tin epidrasi tis sunistamenis
 dunamis toy barous toy kai tis dynamis tis antistasis
   Fol = ma = B+F = mg - bu  (2) 
 opou theoroume ti fora pros ta katw thetiki 
 H diaforiki eksiswsi einai: 
   ma = mdu/dt = b(mg/b - u)  Theoroume v0 = mg/b - oriaki taxytita 
   du/[b(uo-u)] = dt/m => du/(uo-u) = dt*b/m. 
 Oloklirwnoume to prwto melos apo 0 ews u kai to 
 deytero apo 0 ews t opote tha exoume
  -ln(uo - u)  = t*b/m              =>   me oria 0-u aristera kai 0-t deksia 
  [ln(uo - u) - ln(uo-V0)] = -b*t/m =>   opou V0 i arxiki taxutita
  ln[(uo - u)/(uo-V0)] = -b*t/m     =>
  uo - u = (uo-V0)exp(-b*t/m)       =>
  u = V0*exp(-b*t/m) + uo*(1-exp(-b*t/m) (3) opou uo=mg/b kai V0 arxiki taxutita
  H (3) apotelei tin geniki analutiki lusi

  Gia tin methodo toy Euler tha xreiastei na kanoume to vima:
     a = g - u*b/m    H taxutita einai ti stigmi t_i 
     u = u + a*dt     H taxytita einai twea ti stigmi t_i+1
 
  Gia tin methodo tou Euler-Cromer exoume:
     a = g - u*b/m    H paragwgos ti stigmi t_i
     unew = u + a*dt  H taxitita ti stigmi t_(i+1)
     a = g - unew*b/m H epitaxunsi ti stigmi t_(i+1)
     u = u + a*dt     H taxytita ti stimi t_(i+1) meta apo vima Euler-Cromer 
                      opou xrisimopoioume tin paragwgo ti stigmi t_(i+1) gia 
                      na upologisoume tin xroniki ekseliksi tis taxytitas 

  To programma trexei gia:
  Arxiki taxutita : 0m/s
  Mass            : 0.01 kg  (10gr)
  b               : 0.1  Ns/m
  tfin            : 0.5 sec
  dt              : 0.01 kai 0.001
 
'''
import numpy as np
import matplotlib.pyplot as plt


# H synartisis TheorSol douleuei toso me sugkekrimeni timi
# gia ti metavliti times oso kai me ti xrisi pinaka
def TheorSol(time, Vterminal, Vinit, b, mass): 
    return Vinit*np.exp(-time*b/mass) + Vterminal*(1-np.exp(-time*b/mass))

def Deriv(velocity, b, mass, g):
    return g - velocity * b/mass

def Euler(TDeriv, Vterm, Vinit, g, b, m, tstart, tfin, dt):
    time     = tstart         # arxikos xronos
    v        = Vinit          # arxiki taxytita
    Velocity = []             # Pinakas taxytitwn 
    Time     = []             # Pinakas xronwn
    Error    = []             # Pinakas diaforas theoritikis - arithmitikis
    while time < tfin:        # Loop ews otou o xronos ginei isos me 
                              # ton apaitoumeno xrono ekseliksis
        Velocity.append(v)    # apothikeusi ti pliroforias se pinaka
        Time.append(time)
        theory = TheorSol(time,Vterm,Vinit,b,m)  # H theoritiki lisi sto time
        Error.append(np.abs(theory - v))         # Diafora Theory - Euler
        dudt = TDeriv(v,b,m,g)                   # klisi tis paragwgou
        v    = v + dudt * dt                     # Vima Euler
        time = time + dt
    return Time, Velocity, Error

def EulerCromer(TDeriv, Vterm, Vinit, g, b, m, tstart, tfin, dt):
    time     = tstart         # arxikos xronos
    v        = Vinit          # arxiki taxytita
    Velocity = []             # Pinakas taxytitwn 
    Time     = []             # Pinakas xronwn
    Error    = []             # Pinakas diaforas theoritikis - arithmitikis
    while time < tfin:        # Loop ews otou o xronos ginei isos me 
                              # ton apaitoumeno xrono ekseliksis
        Velocity.append(v)    # apothikeusi ti pliroforias se pinaka
        Time.append(time)
        theory  = TheorSol(time,Vterm,Vinit,b,m) # H theoritiki lisi sto time
        Error.append(np.abs(theory - v))         # Diafora Theory - Euler
        dudt    = TDeriv(v,b,m,g)                # klisi tis paragwgou
        v_new   = v + dudt * dt                  # Vima Euler
        dudt    = TDeriv(v_new,b,m,g)            # H nea epitaxinsi 
        v       = v + dudt * dt                  # Vima EulerCromer:
                                                 # xrisimopoiisi 
        time = time + dt                         # tis neas epitaxynsis

    return Time,Velocity,Error

#... Kurio programma

V0     = float(input("Specify the initial velocity: "))
mass   = float(input("Specify the mass of the object: "))
bcon   = float(input("Specify ti stathera tis antistasis D: "))
tfin   = float(input("Specify the final time: "))
nsteps = int(input("Specify the number of cases for the time step: "))
TheTime, TheVelocity, TheError = [],[],[]
tst    = 0   # arxiki xroniki stigmi
g      = 9.81                 # acceleration of gravity
Vterminal = mass*g/bcon       # Oriaki taxutita

labels,legends = [],[]
for icase in range(nsteps):
    strng = 'Enter the time step for %.d case ' % icase
    leg = input(strng)
    dt = float(leg)
    lbl1 = 'Euler - dt='+leg
    lbl2 = 'Euler-Cromer - dt='+leg
    labels.append(lbl1)              # Dimiourgia labels and legends
    labels.append(lbl2)
    legends.append(leg)              # for the plotting
#... Euler    
    Time, Velocity, Error = [],[],[]                # Orismos twn pinakwn 
    Time,Velocity,Error = Euler(Deriv,Vterminal,V0,g,bcon,mass,tst,tfin,dt)
    TheTime.append(Time)                            # Apothikeusi twn pinakwn
    TheVelocity.append(Velocity)                    # se pinakes pinakwn
    TheError.append(Error)                          # To icase stoixeio kathe
    del Error                                       # sunthetou pinaka einai 
    del Time                                        # enas pinakas 
    del Velocity
#... Euler-Cromer
    Time, Velocity, Error = [],[],[]                # Orismos twn pinakwn 
    Time,Velocity,Error = EulerCromer(Deriv,Vterminal,V0,g,bcon,mass,tst,tfin,dt)
    TheTime.append(Time)                            # Apothikeusi twn pinakwn
    TheVelocity.append(Velocity)                    # se pinakes pinakwn
    TheError.append(Error)                          # To icase stoixeio kathe
    del Error                                       # sunthetou pinaka einai 
    del Time                                        # enas pinakas 
    del Velocity

#... Gia to grafima tis theoritikis kampulis

ThTime=np.linspace(tst,tfin,1001)                # fill the time range
ThVelo=TheorSol(ThTime,Vterminal,V0,bcon,mass)   # Dimiourgia tis theoritikis 

#... Plotting 
comm=['g:', 'r-.', 'b--', 'C1-','mv']
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(ThTime, ThVelo, 'b-',label='Theory')
for ic in range(nsteps):
    plt.plot(TheTime[2*ic],TheVelocity[2*ic],comm[2*ic],label=labels[2*ic])
    plt.plot(TheTime[2*ic+1],TheVelocity[2*ic+1],comm[2*ic+1],label=labels[2*ic+1])
plt.title('Motion in a fluid with Drag')
plt.xlabel('Time (sec)')
plt.ylabel('Velocity, V($m/s$)')
plt.xticks(np.linspace(0,tfin,6))    #Kathorismos upodiairesewn
plt.yticks(np.linspace(0,Vterminal+0.02,11))
plt.ylim(0.,1.05)
plt.legend(loc='lower right')
plt.axhline(y=Vterminal,linestyle='--',color='green',zorder=-1)
plt.text(0.01,0.93,r'$V_{{terminal}} =$ {0:5.2f}'.format(Vterminal))
plt.grid(True)

plt.subplot(1,2,2)
for ic in range(nsteps):
    plt.plot(TheTime[2*ic],TheError[2*ic], comm[2*ic], label=labels[2*ic])
    plt.plot(TheTime[2*ic],TheError[2*ic], comm[2*ic+1], label=labels[2*ic+1])
plt.title("|Theoretical - Computinal|")
plt.xlabel('Time (sec)')
plt.ylabel('Difference, T($^o$C)')
plt.xticks(np.linspace(0,tfin,6))
plt.legend(loc='upper right')
plt.grid(True)
#
plt.tight_layout()
#
plt.savefig('hm06_prob04.pdf')
#
plt.show()
    
