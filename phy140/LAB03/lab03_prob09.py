#!/usr/bin/python3

'''
Ta stoixeia mporoun na dwthoun apo to pliktrologio ena pros ena
i na ta grapsete se ena arxeio p.x. MyNumbers.dat, ena se kathe grammi
kai meta na dosete sto terminal tin entoli

python3 lab03_prob09.py < MyNumbers.dat

opou < einai i entoli redirection tis linux gia eisagwgi stoixeiwn apo ta
deksia stin entoli aristera. To MyNumbers.dat paizei me ton tropo ayto to
rolo toy pliktrologiou
'''

MyNumbers=[]    # Dimiourgia mias kenis lists

MyNumbers +=[int(input("Give number  1 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  2 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  3 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  4 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  5 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  6 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  7 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  8 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number  9 "))]   # Eisagwgi enos akeraiou arithmou
MyNumbers +=[int(input("Give number 10 "))]   # Eisagwgi enos akeraiou arithmou

themx = max(MyNumbers)
themn = min(MyNumbers)
MyNumbers_org=MyNumbers
MyNumbers.sort()              # Taksinomisi se ayksousa seira
print("sort:auksousa: ",MyNumbers_org,MyNumbers)
MyNumbers.sort(reverse=True)  # Taksinomisi se fthinousa seira
print("sort:fthinousa: ",MyNumbers_org,MyNumbers)

'''
Xrisimopoiontas numpy
import numpy as np
MyNumbers = np.array(MyNumbers)
themx = MyNumbers.max()            # idiotites twn pinakwn
themn = MyNumbers.min()          # idiotites twn pinakwn
MySort= sorted(MyNumbers,reverse=True)  # Xrisi tis methodou sorted tis python
                                        # gia taksinomisi kata fthinousa seira
                                        # dimiourgontas mia nea list kai exontas
'''                                        # tin arxiki lista ametavliti

print("The initial unsorted list is\n",MyNumbers)
print("The maximum number of the list is ",themx)
print("The minimum number of the list is ",themn)
print("The list sorted is\n",MySort)
