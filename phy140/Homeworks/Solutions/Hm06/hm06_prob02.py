#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def y(t):
    return (C*vo*np.sin(theta0) + g*C*C)*(1-np.exp((-t)/C)) - g*C*t

def yderiv(t):
    return (vo*np.sin(theta0) + g*C)*np.exp(-t/C) - g*C

def x(t):
    return C*vo*np.cos(theta0)*(1-np.exp((-t)/C))

def newton(x0, f, df, eps, istepmx):
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error    # The new solution 
        x0 = x1            # The new solution becomes the old solution for the
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1
            break
#
    return x0,flag,istep

def check_graphical_sol(xmn,xmx):
    time = np.linspace(xmn,xmx,10000)
    ypos = y(time)
    plt.plot(time,ypos)
    plt.show()
    return

C = 10
g = 9.8
theta0 = np.pi/4
vo = 49

check_graphical_sol(0,10)

tfl_guess  = 4.0           # Na simeiwthei oti uparxoun times arxikou xronou 
prec = 1E-8                # pou den brisketai lusi gia megales gwnies
itmx =  100
flight_time,flag,istep=newton(tfl_guess,y, yderiv, prec, itmx)
flyt45 = flight_time
velinekes = x(flight_time)

print("Xronos ptisis = %12.8f"%(flight_time))
print("Belinekes = % 12.8f"%(velinekes))

'''
  (b)
'''
Xa, Va, ToF=[], [], []
outfile=open("ranges.dat","w")
angles = np.linspace(1,90,90)
for angle in angles:
    theta0 = angle*np.pi/180    # conversion to radians
    flight_time,flag,ister=newton(tfl_guess,y, yderiv, prec, itmx)
    if (flag !=0) :
        print("For angle:%3.0f - flag:%1i - Time-of-flight:%6.3f"%
              (angle,flag,flight_time))
        break
    tfl_guess = flight_time      # Use the time-of-flight as a guess solution
                                 # for the next angle 
    velinekes = x(flight_time)
    Xa +=[angle]
    Va +=[velinekes]
    ToF+=[flight_time]
    if (angle%10 == 0 and angle>0 and angle <90):
        outfile.write("%2i %12.8f\n"%(angle, velinekes))
outfile.close()
'''
  (c)
'''
outfile=open("projectile.dat","w")
theta0 = np.pi/4     # 45 moires gwnia
timestep = 0.1
time = 0
inflight = True
while inflight:
    if time <= flyt45:
        xpos = x(time)
        ypos = y(time)
        outfile.write("%8.3f %8.3f\n"%(xpos,ypos))
    else:
        xpos = x(flyt45)
        ypos = y(flyt45)
        outfile.write("%8.3f %8.3f\n"%(xpos,ypos))
        break
    time += timestep
outfile.close()

'''
  (d)
'''
X,Y = [],[]
infile=open("projectile.dat","r")
for line in infile:
    xp,yp = line.strip().split()
    X.append(float(xp))
    Y.append(float(yp))
infile.close()

Angle, Veli = [],[]
infile=open("ranges.dat","r")
for line in infile:
    th,xv = line.strip().split()
    Angle.append(float(th))
    Veli.append(float(xv))
infile.close()

plt.figure(figsize=(6,6))
plt.plot(X,Y,'b-')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.ylim(0,1.1*max(Y))
plt.xlim(0,1.1*max(X))
plt.savefig("projectile.pdf")
plt.show()

plt.figure(figsize=(6,6))
plt.plot(Angle,Veli,'bo')
plt.plot(Xa,Va,'r-')
plt.xlabel(r'Initial Angle, $\theta_0$  (Degrees)')
plt.ylabel('Velinekes, r (m)')
plt.ylim(0,1.1*max(Veli))
plt.xlim(0,90)
plt.savefig("ranges.pdf")
plt.show()

plt.figure(figsize=(6,6))
plt.plot(Xa,ToF,'b-')
plt.xlabel(r'Initial Angle, $\theta_0$  (Degrees)')
plt.ylabel('Time of Flight, t (s)')
plt.ylim(0,1.1*max(ToF))
plt.xlim(0,90)
plt.show()


exit()

