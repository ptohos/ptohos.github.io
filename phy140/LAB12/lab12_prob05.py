#!/usr/bin/python3

'''Xrisimopoioume ti methodo tou metasximatismou gia na 
   dimiourgisoume mia katanomi tuxaiwn arithwm me PDF P(x) 
   ksekinontas apo omoiomorfa katanemimenous arithmous se
   kapoio diastima [A,B]
   Sti periptwsi toy provlimatos mas dinetai i PDF=P(x)=sin(x) 
   Epomenws sumfwna me ti methodo: P(x)dx = P(y)dy 
   Alla P(y) einai omoiomorfi katanomi opote tha exoume:
     sin(x)dx=dy
   Oloklirwsi tha dosei tin CDF(x) => 
     integral( sin(x)dx) = y => y = -cos(x)  
   kai prepei na lysoume ws pros x, na antistrefoume ti CDF diladi 
     x = arc cos(-y) diladi x = acos(-y)
   Epomenws pernontas x sumfwna me ti sxesi acos(-y) tha 
   oi x-times tha einai katanemimenes sumfwna me tin PDF P(x)=sin(x)

   ****Na simeiwthei oti i PDF(x) tha prepei na einai >0 gia ola ta x *** 

   Estw oti theloyme ta x ayta na pernoun times metaksu 0 kai pi
   Analoga me to diastima timwn tou x poy mas endiaferei tha prepei 
   na kanonikopoiisoume tin PDF pou antistoixei sto diastima endiaferontos.
   Diladi tha prepei na orisoume mia PDF' tetoia wste PDF' = PDF/norm 
   opou norm = integral_a ^b PDF(x)dx   opou a kai b ta oria toy 
   diastimatos endiaferontos. 
   Epomenws integral_0 ^y dy = integral_a ^x [PDF'(x)dx] => 
             y = integral_a ^x [PDF'(x)dx] = integral_a^x[PDF(x)dx]/norm
   Stin periptwsi mas poy a = 0 kai b = pi tha exoume 
   norm = Integral_(0) ^(+pi) [PDF(x)dx)] = -cos(x)|_0 ^pi = 2 kai 
   epomenws PDF'(x) = PDF(x)/2 
   Ara y = { (-cos(x))|_(0)^(x) }/2 => 2y = -cos(x) +1 => cos(x) = 1 - 2*y
   => x = acos(1-2*y)
   '''


import numpy as np
from math import acos
import matplotlib.pyplot as plt
from random import seed, random

def PDF(x):
    return np.sin(x)

xlo = float(input("Give the lower value of the desired x-interval [0.0] "))
xup = float(input("Give the upper value of the desired x-interval [3.14] "))
Ntries = int(input("How many random numbers to generate [100K]? "))

seed(123456)

yvl = []
norm = -(np.cos(xup) - np.cos(xlo))
for itry in range(Ntries):
    xv = random()           # epilogi tuxaias timis metaksu [0,1)
    xv = 1 - norm*xv
    yvl.append(acos(xv))

plt.figure(figsize=(6,6))
cont,xbinval,intr=plt.hist(yvl,bins=100,range=(0,np.pi),density=True,
                           histtype='step',color='g')

ypdf=PDF(xbinval)/norm
plt.plot(xbinval,ypdf,'b-',label=r'PDF:sin(x)')
plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number distributed according to $sin(x)$')
plt.axis([0,np.pi,0.,0.55])
plt.grid(True)
plt.legend()
plt.show()
