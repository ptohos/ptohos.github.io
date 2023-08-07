#!/usr/bin/python3

import matplotlib.pyplot as plt
''' 
Klisi tis parakatw vivliothikis wste na apothikeusoume 
polla grafimata se polles selides sto pdf arxeio
'''
from matplotlib.backends.backend_pdf import PdfPages 

y=[]                                # Dimiourgia mias listas

fig1 = plt.figure()                 # Dimiourgia mias eikonas gia
                                    # tin apotypwsi tou grafimatos
for i in range(5):
    y.append(2*i-1)                 # Gemizoume ti lista me 5 stoixeia
                                    # symfwna me tin sxesi
    
plt.plot(y)                         # Mporoume na kanoume to grafima
                                    # dinontas mono ton pinaka twn timwn y
                                    # H python ypothetei oti oi times tou
                                    # einai oi theseis twn stoixeiwn tis
                                    # y-pinaka. Stin prokeimeni periptwsi
                                    # exoume 5 stoixeia me theseis 0,1,2,3,4
                                    # Opote perimenoume oti oi times toy
                                    # x-aksona tha einai 0,1,2,3,4

fig2 = plt.figure()                 # Dimiourgia mias neas eikonas
plt.plot(y,'ro')                    # Dimiourgia grafimatos me simeia se
                                    # kokkino xrwma ('r') kai kuklous ("o")
plt.xlabel('X-values')              # Vazoume etiketta ston x-aksona
plt.ylabel('Y-values')              # etiketta ston y-aksona
plt.title('My first plot',size=20)  # Genikos tupos

pp = PdfPages("Myplot.pdf")         # Anoigma enos pdf arxeiou onoma Myplot.pdf 
pp.savefig(fig1)                    # Apothikeusi tis prwtis eikonas      
pp.savefig(fig2)                    # Apothikeusi tis deuteris eikonas
pp.close()                          # Kleisimo toy arxeiou

