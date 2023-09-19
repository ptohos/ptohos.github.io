#!/usr/bin/python3

import numpy as np
import matplotlib as plot

#=======================================================================
# Gia tin eyresi tis perimetroy toy n-polugwnou to opoio einai
# eggegrammeno se enan kuklo diametrou d tha prepei na ypologisoume
# to mikos tis pleuras tou polugwnou. To mikos tis pleyras toy
# polugwnou einai to mikos tis xordis pou enwnei dyo diadoxikes
# korufes tou pologwnou pou einai simeia tis perifereias toy kuklou.
# Alla to trigwno pou sximatizetai me ta dyo aytes korufes kai to
# kentro toy kuklou einai isoskeles (oi 2pleures einai oi aktines
# tou kuklou. Epomenws to ypsos apo tin korufi pou sympiptei me tin
# koryfi tou kuklou pros tin pleura tou polugwnou einai kai dixotomos
# tis antistoixis gwnias. Temnei episis tin pleura tou polugwnou
# sto meso. Epomenws an i gwnia einai theta tote to miso tis pleuras
# tou polugwnou tha einai l/2 = R*sin(theta/2) => l = 2*R*sin(theta/2)=>
# l = d * sin(theta/2).
# H gwnia tou theta = 2*pi/n. Opote i pleura tou polugwnou einai
# l = d * sin(pi/n) => perimetros = n * d * sin(pi/n)
#=======================================================================

d = float(input("Please give the diameter of the circle "))

polygons=[3,4,5,100,10000,1000000, 100000000]
perimetroi=[]                     # Dimiourgia kenis listas perimetrwn
ndif_polugons = np.size(polygons)   # Poses periptwseis na eksetasoume

string1 = "Polugon"
string2 = "Perimetros"
print("%12s %16s" % (string1, string2))
for npoly in polygons:   # To npoly tha parei times 3,4,5,100... apo ti lista
    side = d * np.sin(np.pi/npoly)   # pi sunartisi pou dinei to pi
    perimetros = npoly*side
    print("%12d %18.15f"%(npoly,perimetros))
print("Notice that as the number of sides of the polygon increases\n"\
      "the perimeter aproaches the valus of pi = ",np.pi)

    


