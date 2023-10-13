#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def pt(LV):        #<< to 4-dianusma (E,px,py,pz) orizetai ws LorentzVector (LV)
    return np.sqrt(LV[1]**2 + LV[2]**2)

def magnitude4Vec(LV):
    '''Ypologismos toy metrou enos 4-dianusmatos'''
    return np.sqrt(LV[0]**2 - LV[1]**2 - LV[2]**2 - LV[3]**2)

def magnitude3Vec(LV):
    '''Ypologismos toy metrou tou xwrikou merous enos 4-dianusmatos'''
    return np.sqrt(LV[1]**2 + LV[2]**2 + LV[3]**2)
        

def Get_Mass(LV1,LV2):
    ''' Dexetai ws orismata 2 LorentzVectors (4-dianusmata)
        twn duo swmatidiwn pou einai ta proionta
        diaspasis enos alloy swmatidiou ti maza tou opoiou
        theloume na vroume
        H function epistrefei ti maza tou diaspwmenou swmatidioy
        kai to 4-dianusma tou (E,px,py,pz) '''
    LV=[]               #<< orizoume ena neo LV 
    for j in range(len(LV1)):
        LV += [ LV1[j]+LV2[j] ]
    mass = magnitude4Vec(LV)
    return mass,LV

#======================
#  Kurio programma
#======================
filename = input("Give the name of the data file ")
inpfile = open(filename,'r')
iline = 0
Ene1, Px1_mom, Py1_mom, Pz1_mom=[],[],[],[]
Ene2, Px2_mom, Py2_mom, Pz2_mom=[],[],[],[]
for line in inpfile:
    iline+=1
    E1,px1,py1,pz1,E2,px2,py2,pz2 = line.strip().split()
    try:
        Ene1   += [float(E1)]
        Px1_mom+= [float(px1)]
        Py1_mom+= [float(py1)]
        Pz1_mom+= [float(pz1)]
        Ene2   += [float(E2)]
        Px2_mom+= [float(px2)]
        Py2_mom+= [float(py2)]
        Pz2_mom+= [float(pz2)]
    except:
        print("Problems reading line\n",iline,line)
        continue
    
print("The number of good pairs that were read from the file is:",len(Ene1))
Zmass = []
ptLep = []
for j in range(len(Ene1)):
    LV1 = [Ene1[j], Px1_mom[j], Py1_mom[j], Pz1_mom[j]]  # 4-dianusma
    LV2 = [Ene2[j], Px2_mom[j], Py2_mom[j], Pz2_mom[j]]  # 4-dianusma 
    pt1 = pt(LV1)
    pt2 = pt(LV2)
    #<< Afinoyme to zeugos an ena toulaxiston exei pt<20
    if pt1 < 20 or pt2 < 20 : continue
    mass,ZLV = Get_Mass(LV1,LV2)
    Zmass +=[mass]
    ptLep +=[pt1]
    ptLep +=[pt2]
print("The number of pairs with both leptons with pt>20 is:",len(Zmass))

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
Zcontent,Zv,rcon=plt.hist(Zmass,40,range=(50,130),facecolor='b',histtype='step')
plt.xlabel("Mass $Z^0_{e^+e^-}$ (GeV/$c^2$)")
plt.ylabel("No of pairs/(2 GeV/$c^2$)")
plt.xlim(60,120)
plt.grid(True)
fileout=open("hm03_prob05.dat","w")
binsz=2.0   
for i in range(len(Zcontent)):
    fileout.write("%5.1f %5d\n"%(Zv[i]+binsz/2,Zcontent[i]))
fileout.close()
#
plt.subplot(1,2,2)
ptcontent,ptv,rc=plt.hist(ptLep,50,range=(0,100),facecolor='k',histtype='step')
plt.xlabel("Lepton $p_T$ (GeV/c)")
plt.ylabel("No. of leptons/(2 GeV/c)")
plt.xlim(0,60)
plt.grid(True)
plt.tight_layout()
plt.show()
