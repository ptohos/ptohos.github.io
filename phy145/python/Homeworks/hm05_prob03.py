#!/usr/bin/python3

'''===================================================
... Gia na upologisoume ta reumata se kathe klado tou
... kuklwmatos pou dinetai, tha prepei arxika na 
... efarmosoume tous kanones Kirchhoff stous vroxous 
... kai na kataliksoume se ena sustima eksiswsewn to 
... opoio tha lusoume me grammiki algevra.
...
... Theoroume oti tous duo broxous, aristera auton pou
... periexei tis piges E1 kai E2 kai deksia auton pou 
... periexei tis piges E2 kai E2. Theoroume episis oti
... to reuma kineitai kai stous duo broxous antitheta
... me ti fora twn deiktwn tou rologiou (opws deixnei
... kai to sxima).

... Oi kanones Kirchhoff:
...  1os: I diafora dunamikou se kleisto 
...       broxo einai miden. Prosoxi xreiazetai sto 
...       prosimo tis diaforas dunamikou sta akra pigwn
...       An sunantatai prwta thetikos polos to prosimo 
...       einai arnitiko, diaforetika thetiko. 
...       An i fora tou reumatos se mia antistasi einai
...       antitheti me ti fora kinisis sto broxo, to 
...       prosimo tis ptwsis tasis stin antistasi einai 
...       thetiko diaforetika arnitiko (xanetai energeia)
...  2os: To athroisma twn eiserxomenwn reumatwn se 
...       se ena komvo isoutai me to athroisma twn 
...       ekserxomenwn apo ton komvo reumatwn.
...
... Efarmogi 1ou kanona ston aristero broxo:
...   -I1R1 - E1 - I1R1 + E2 + I2R2 = 0  (1)
... Efarmogi 1ou kanona ston deksia broxo:
...   -I3R1 - I2R2 - E2 - I3R1 + E2 = 0  (2)
... Efarmogi tou 2ou kanona ston komvo a
...   I3 = I1 + I2                      (3)
...
... Aplousteuontas tis eksiswseis (1),(2) kai (3):
...   -2R1 * I1 + R2 * I2 = E1 - E2     (1)
...   -2R1 * I3 - R2 * I2 = 0           (2)
...    I3 = I1 + I2                     (3)
... Antikatastasi twn arithmitikwn dedomenwn dinei:
...     I3 = I1 + I2 =>               I1 +  I2 -  I3 =  0  (A)
...   -2*2 * I1 + 4 * I2 = 3 - 6 => -4I1 + 4I2 + 0I3 = -3  (B)
...   -2*2 * I3 - 4 * I2 = 0     =>  0I1 - 4I2 - 4I3 =  0  (C)
...    Prosthetontans tis 2 proigoumenes exoume:
...   -4(I1+I3) = -3 => I1 + I3 = +3/4               (D)  
...    Antikatastasi tis (A) sti (D): 2I1 = -I2+3/4  (E)
...    Thetontas tin (E) stin (B): +2I2 -3/2 + 4I2 = -3
...    => +6I2 = 3/2 - 3 => 6I2 = -3/2 => I2 = -1/4  (F)
...    Epomenws apo (E) kai (F) exoume:   I1 = +1/2  (G)
...    kai apo (F) kai (G) stin (A):      I3 = +1/4  (H) 
   ==================================================='''

import numpy as np

# Arrays tou systimatos twn 3 eksiswsewn me 3 agnwstous:
# Oi suntelestes twn eksiswsewn (A),(B),(C)
#=======================================================
R = np.array([[1,1,-1],[-4,4,0],[0,-4,-4]])   # Pinakas suntelestwn twn agnwstwn
C = np.array([0,-3,0])                      # Pinakas statherwn orwn

#... Lusi
#...=======
x = np.linalg.solve(R,C)

#... Apotelesmata
#... =============
print(40*('-'))
print('  Apotelesmata analusis kuklwmatos')
for i in range(len(x)):
    print("  To reuma I%d einai: %5.2fA"%(i+1,x[i]))
print(40*'-')
exit()
    
