#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#read data
time, counts, error = np.loadtxt('SemiLogData.dat',unpack=True)

#theoretical curve
t_half = 14              # time of half life: 14 days
tau = t_half/np.log(2)   # ekthetikos xronos zwis
N0 = 8200.               # arxikos rythmow diaspasis
t  = np.linspace(0, 180, 181)
N  = N0 * np.exp(-t/tau) # ekthetiki diaspasi

# create the plot
plt.figure(1, figsize=(9.5,4))  # to megethos toy canva toy sxediou

plt.subplot(1,2,1)       # opws eidame ayto mporei na grafei kai ws subplot(121)
                         # Simainei ta plots tha ginoun se 1 grammi kai 2 stiles
                         # kai to sygkekrimeno grafima tha mpei stin aristeri
                         # pleyra toy canva
# Grammiki klimaka                        
plt.plot(t, N, color='C0', label = "theory")
plt.plot(time, counts, 'oC1', label = "data")
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')
plt.grid(True)
#
# Logaritmiki klimaka
plt.subplot(1,2,2)      # Topothetisi tou grafimatos sti deksia thesi
plt.semilogy(t, N, color='C0', label='theory')
plt.semilogy(time, counts, 'oC1', label='data')
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')
plt.grid(True)
#
'''
Ruthimisi twn apostasewn metaksu twn subplots
 gia na fainontai kalytera oi klimakes twn axonwn
 An den tin kalesoume, tote i klimaka toy y-aksona
 sto deksi grafima peftei sto aristero grafima
'''

plt.tight_layout()

'''
   An thelete perissotero control tou xwrou gurw apo
   ta subplots tha prepei na xrisimopoiuthei i sunartisi

   plt.subplots_adjust(left=None, right=None, bottom=None, top=None
                       wspace=None, hspace=None)

   Oi parametroi wspace and hspace ruthmizoun to euros kai to ypsos tis
   apostasis anamesa sta grafimata, enw oi ypoloipes parametroi ruthmizoun 
   tin apostasi apo to aristero, deksi, panw kai katw meros tou canva 
'''
#
plt.savefig('SemiLogPlot.pdf')
#
plt.show()
