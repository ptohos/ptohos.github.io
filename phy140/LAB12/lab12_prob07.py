import numpy as np
import matplotlib.pyplot as plt
from random import seed, random


n = 100
seed(12345678)

fpos1 =[]
fpos2 =[]
fpos3 =[]
fpos4 =[]
fpos5 =[]
fpos6 =[]
fpos7 =[]
nsteps = np.array([8,16,32,64,128,256,512])
for j in range(int(1E7)):
    p = 0.0
    d = 0.0
    for i in range(512):
        if (random() >= 0.5):
            p = p + 1
        else:
            p = p - 1
        if i == 7:
            fpos1.append(p)
        elif i == 15:
            fpos2.append(p)
        elif i == 31:
            fpos3.append(p)
        elif i == 63:
            fpos4.append(p)
        elif i == 127:
            fpos5.append(p)
        elif i == 255:
            fpos6.append(p)
        elif i == 511:
            fpos7.append(p)
        else:
            pass
        
fpos1 = np.array(fpos1)
fpos2 = np.array(fpos2)
fpos3 = np.array(fpos3)
fpos4 = np.array(fpos4)
fpos5 = np.array(fpos5)
fpos6 = np.array(fpos6)
fpos7 = np.array(fpos7)
msd1 = sum(fpos1**2)/len(fpos1)
msd2 = sum(fpos2**2)/len(fpos2)
msd3 = sum(fpos3**2)/len(fpos3)
msd4 = sum(fpos4**2)/len(fpos4)
msd5 = sum(fpos5**2)/len(fpos5)
msd6 = sum(fpos6**2)/len(fpos6)
msd7 = sum(fpos7**2)/len(fpos7)
msd = np.array([msd1, msd2, msd3, msd4, msd5, msd6, msd7])
print(msd1, msd2, msd3, msd4, msd5, msd6, msd7)

plt.figure(figsize=(8,6))
cont,xbins,igno=plt.hist(fpos1,bins=400,range=(-200,200),density=True,histtype='step')
plt.xlabel('Position')
plt.ylabel('Number')
plt.xlim(-50,50)
plt.title('10M walkers with 8 steps: MSD = %6.2f'%msd1) 
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
cont,xbins,igno=plt.hist(fpos4,bins=400,range=(-200,200),density=True,histtype='step')
plt.xlabel('Position')
plt.ylabel('Number')
plt.xlim(-50,50)
plt.title('10M walkers with 64 steps: MSD = %6.2f'%msd4) 
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
cont,xbins,igno=plt.hist(fpos7,bins=400,range=(-200,200),density=True,histtype='step')
plt.xlabel('Position')
plt.ylabel('Number')
plt.xlim(-150,150)
plt.title('10M walkers with 512 steps: MSD = %6.2f'%msd7) 
plt.grid(True)
plt.show()

p = np.polyfit(nsteps,msd,1)
xsteps=np.arange(0,600)
linfit = xsteps*p[0]+p[1]
plt.figure(figsize=(8,6))
plt.plot(nsteps,msd,'bo')
plt.plot(xsteps,linfit,'r-')
plt.xlabel('Number of Steps')
plt.ylabel('Mean Square Distance')
plt.xlim(0,600)
plt.ylim(0,600)
plt.grid(True)
plt.show()
