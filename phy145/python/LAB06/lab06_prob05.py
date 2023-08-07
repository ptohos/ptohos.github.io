#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def interpolate(TargetV,PosI,PosF):
    slope = (PosF[1] - PosI[1])/(PosF[0] - PosI[0])
    pos2 = PosI[1] + slope * (TargetV - PosI[0])
    return pos2

def discharging(Vtarget, Vst, T0, tstep, Resist, Cap):
    T=[]
    V=[]
    tau = Resist*Cap
    t = T0
    istp = 0
    V += [Vst]
    T += [T0]
    while V[istp] >= Vtarget or t == T0 :
        istp += 1 
        t += tstep
        T += [t]
        V += [Vst*np.exp(-t/tau)]

    return T, V

def charging(Vtarget, Vst, T0, tstep, Resist, Cap):
    T=[]
    V=[]
    tau = Resist*Cap
    t = T0
    istp = 0
    V += [0]
    T += [T0]
    while V[istp] <= Vtarget or t == T0 :
        istp += 1 
        t += tstep
        T += [t]
        V += [Vst*(1-np.exp(-t/tau))]
    return T, V

#====================
# Initial conditions
# dt = 1E-5
#====================
Vp = float(input("Insert the value of the Voltage source[Volts] "))
R  = float(input("Insert the value of the resistance[Ohm] "))
C  = float(input("Insert the vaue of the capacitance[uF] "))
t0 = float(input("Insert the initial time "))
dt = float(input("Insert the time step "))
Vfd= float(input("Insert the value of the target voltage in discharge mode "))
Vfc= float(input("Insert the value of the target voltage in charging mode "))

# Charging
#=============
tcharge, vcharge = charging(Vp*Vfc, Vp, t0, dt, R, C)
ist = len(tcharge)-1
vlast  = vcharge[ist]
tlast  = tcharge[ist]
vblast  = vcharge[ist-1]
tblast = tcharge[ist-1]
vt0pos=np.zeros(2)
vt1pos=np.zeros(2)
vt0pos[1] = tblast
vt0pos[0] = vblast
vt1pos[1] = tlast
vt1pos[0] = vlast
vfin = Vp*Vfc
tcfin = interpolate(vfin,vt0pos,vt1pos)
vcharge[ist] = vfin
tcharge[ist] = tcfin
print(f'The time to charge to {Vfc:%} of the final voltage is {tcfin:5.4f}s')

# Dis-charging
#=============
tdscharge, vdscharge = discharging(Vp*(1-Vfd), Vp, t0, dt, R, C)
ist    = len(tdscharge)-1
vlast  = vdscharge[ist]
tlast  = tdscharge[ist]
vblast = vdscharge[ist-1]
tblast = tdscharge[ist-1]
vt0pos = np.zeros(2)
vt1pos = np.zeros(2)
vt0pos[1] = tblast
vt0pos[0] = vblast
vt1pos[1] = tlast
vt1pos[0] = vlast
vfin = Vp*(1-Vfd)
tdfin = interpolate(vfin,vt0pos,vt1pos)
vdscharge[ist] = vfin
tdscharge[ist] = tdfin
print(f'The time to discharge to {(1-Vfd):%} of the final voltage is {tdfin:5.4f}s')

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(tcharge,vcharge,'b-',lw=2)
plt.title('Capacitor Charging')
plt.xlim(0,0.005)
plt.ylim(0,13)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.text(0.003,10,r'$V_p[1- e^{-\frac{t}{RC}}]$')
plt.text(0.003,9.5,r'$V_p = 12V$')
plt.text(0.003,9.0,r'$R = 1000\Omega$')
plt.text(0.003,8.5,r'$C = 1 \mu F$')
plt.text(0.003,8.0,rf'$t_{{98\%V_p}}$ = {tcfin:5.4f}')

plt.axhline(y=Vfd*Vp,color='red',linestyle='--')

plt.subplot(1,2,2)
plt.plot(tdscharge,vdscharge,'b-',lw=2)
plt.title('Capacitor Discharging')
plt.xlim(0,0.005)
plt.ylim(0,13)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.text(0.003,10,r'$V_p e^{-\frac{t}{RC}}$')
plt.text(0.003,9.5,r'$V_p = 12V$')
plt.text(0.003,9.0,r'$R = 1000\Omega$')
plt.text(0.003,8.5,r'$C = 1 \mu F$')
plt.text(0.003,8.0,rf'$t_{{99\%V_p}}$ = {tdfin:5.4f}')
#
plt.tight_layout()
#
plt.savefig('Capacitor.pdf')
plt.show()


    
