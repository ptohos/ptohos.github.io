#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#=======================================
# Apo to anaptugma Taylor:  sin(x) = x - x^3/3!
# sin(x)/x =(x - x^3/3!)/x = 1 - x^2/3!
# Epomenws gia x=0 => J0(x) = sin(x)/x = 1 
#=======================================
def J0(x):
    z = []
    for xval in x:
        if xval == 0:
            z += [ 1]
        else:
            z += [ np.sin(xval)/xval ]
    return z

#=======================================
# Apo to anaptugma Taylor: sin(x) = x - x^3/3! kai cos(x)=1-x^2/2!
# opote: sin(x)/x^2 - cos(x)/x = 1/x - x/3! - 1/x + x/2! = x/3
# Epomenws gia x=0 => J1(x) = sin(x)/x**2 - cos(x)/x = x/3 = 0 
#=======================================
def J1(x):
    z = []
    for xval in x:
        if xval == 0:
            z += [ xval/3 ]
        else:
            z += [ np.sin(xval)/xval**2 - np.cos(xval)/xval ]
    return z

#=======================================
# Apo to anaptugma Taylor: sin(x) = x - x^3/3! kai cos(x)=1-x^2/2!
# opote: (3/x^2-1)sin(x)/x-3cos(x)/x^2 = (3/x^2-1)(x-x^3/3!)/x - 3(1-x^2/2!)/x^2
#  = 3/x^2 - 3/3! - 1 + x^2/3! - 3/x^2 + 3/2 = x^2/3!
# Epomenws gia x=0 => J2(x) = (3/x^22 - 1)sin(x)/x - 3cos(x)/x^2 = x^2/3!
#=======================================
def J2(x):
    z = []
    for xval in x:
        if xval == 0:
            z += [ xval/6 ]
        else:
            z += [ (3/xval**2 - 1)*np.sin(xval)/xval - 3*np.cos(xval)/xval**2 ]
    return z

#=============================================================
# Ayti einai i synartisi gia na paroume ti Bessel sunartisi
# opoiasdipote taksis. Stirizetai se epanaliptiki diadikasia
# xrisimopoiontas tis 2 prwtes sunartiseis
#   J_{n+1} = (2*n+1)/x * J_n - J_(n-1)
# p.x.  J2 = (2*1+1)/x * J1 - J0 = 3/x * (sinx/x**2 - cosx/x) - sinx/x =
#    => J2 = (3/x^2 -1)sinx/x - 3cosx/x^2
# Gia to upologismo tis sunartisis J_{n+1} tha prepei na upologistoun
# oles oi sunartiseis Bessel mexri tin taksi n.
# H sunartisi epistrefeis tis times olwn twn sunartisewn aytwn
#=============================================================
def Jn(n,x):
    vJ0, vJ1, vJ2 = [], [], []
    for xval in x:
        if np.abs(xval) < 1.e-10:     # Prostastia gia times konta sto 0
            j0 = 1 - xval**2/6        # Akoma enas oris sto anaptugma
            j1 = xval/3 - xval**3/30  # sumfawna me ta parapanw
        else:
            j0 = np.sin(xval)/xval
            j1 = j0/xval - np.cos(xval)/xval
        vJ0 += [j0]    # apothikeusi tou J0 gia to x 
        # Gia polu mikra x mporei na paroume arithmitiko sfalma
        # opote prostateyoume to apotelesma thetontas 0
        if np.abs(j1) < 1E-20: j1 = 0.0
        vJ1 += [j1]
        for i in range(1,n):
            j2 = j1 * (2*i+1)/xval - j0
            j0 = j1
            j1 = j2
            vJ2 += [j2]      # Dimiourgia olwn twn orwn apo 2 ews n gia kathe x

    result = []
    if n == 0: result = [vJ0]
    if n == 1: result = [vJ0, vJ1]
    if n > 1 :
        result = [vJ0,vJ1]
        # O tropos pou exei kataskeuastei i list vJ2 exei gia kathe x n-2 orous
        # pou antistoixoun se kathe 1 < k-th <= n oro. Ara gia na paroume ola
        # ta x pou antistoixoun ston oro k tha xreiastei na kanoume slicing
        for k in range(n-1):
            J2 = vJ2[k:len(vJ2):(n-1)]
            result +=[J2]
            
    return result

    
np.seterr(divide='ignore',invalid='ignore')  # Gia na min emfanizei warning gia 
x = np.linspace(0,20,255)                    # diairesi me miden sto compilation
j0 = J0(x)
j1 = J1(x)
j2 = J2(x)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(x,j0,'k-')
plt.plot(x,j1,'b--')
plt.plot(x,j2,'r:')
plt.axhline(color="gray", zorder=-1)
plt.axvline(color="gray", zorder=-1)
plt.text(1.2,0.85,r'$J_{0}(x) = \frac{sin(x)}{x}$',fontsize=12)
plt.text(2.3,0.45,r'$J_{1}(x) = \frac{sin(x)}{x^2} - \frac{cos(x)}{x}$',fontsize=12)
plt.text(3.3,0.32,r'$J_{2}(x) = (\frac{3}{x^2}-{1})\frac{sin(x)}{x} - {3}\frac{cos(x)}{x^2}$',fontsize=12)
plt.text(5,1.0,r'The first 3 Spherical Bessel Functions',fontsize=13)
plt.xlim(0,20)
plt.ylim(-0.25,1.05)
#==========================
# Xrisi tis sunartisis Jn
#==========================
x = np.arange(1e-5,20.,0.001)
n = 3
bessel = Jn(n,x)
#bessel = []
#for xbes in x:
#    bessel.append(Jn(n,xbes))    # gia ola tis takseis <= n
#bessel = np.array(bessel)

plt.subplot(1,2,2)
style=['k-','b--','r-.','m:']
for i in range(n+1):
#    y=bessel[0:len(x),i]
    y = bessel[i]
    plt.plot(x,y,style[i])
    del y
    
plt.axhline(color="gray",zorder=-1)
plt.axvline(color="gray",zorder=-1)
plt.text(1.2,0.85,r'$J_{0}(x) = \frac{sin(x)}{x}$',fontsize=12)
plt.text(2.3,0.45,r'$J_{1}(x) = \frac{sin(x)}{x^2} - \frac{cos(x)}{x}$',fontsize=12)
plt.text(3.3,0.32,r'$J_{2}(x) = (\frac{3}{x^2}-{1})\frac{sin(x)}{x} - {3}\frac{cos(x)}{x^2}$',fontsize=12)
plt.text(5.3,0.22,r'$J_{3}(x) = (\frac{15}{x^3}-{6})\frac{sin(x)}{x} - (\frac{15}{x^2}-1)\frac{cos(x)}{x}$',fontsize=12)
plt.text(5,1,r'The first 4 Spherical Bessel Functions',fontsize=13)
plt.xlim(0,20)
plt.ylim(-0.25,1.05)

plt.tight_layout()

plt.show()
