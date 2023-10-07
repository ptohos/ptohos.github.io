#!/usr/bin/python3

import numpy as np
import matplotlib as plot

# Programma gia tin metatropi enos dekadikou arithmou apo to
# dekadiko systima arithmisis sto dyadiko systima arithimis

def decimalToBinary(num, k_digits) :

        duadikos = ""
        # o arithmos toy dekadikou systimatos
        akeraio_tmima = int(num)             # akeraio meros tou arithmou 
        dekadiko_tmima = num - akeraio_tmima # dekadiko meros tou arithmou 

	# Prwta metatropi tou akeraiou merous sto duadiko systima
        while (akeraio_tmima) : 
		
                ypol = akeraio_tmima % 2   # Ypoloipo tis diairesis me 2 
                duadikos += str(ypol);     # Apothikeusi tou duadikoi (psifio
                                           # pros psifio) se metavliti tupou
                                           # string

                akeraio_tmima //= 2        # To neo akeraio tmima tha einai
                                           # to piliko tis diairesis
                                           # tou proigoumeno me to 2
	
	# Grafi tis grammatoseiras pou krata ta
        # psifia tou duadikou se anapodi seira 
        duadikos = duadikos[ : : -1] 

	# Euresi tis apeikonisisi tou dekadikou tmimatos tou arithmou
        # sto duadiko systima
        duadikos += '.'           # Topothetisi . gia na deiksoume to dekadiko

        while (k_digits) :
                # To provlima einai oti sumfwna me tous
                # algorithmo pou perigrapsame, uparxoun
                # dekadikoi arithmou pou odigoun se apeiro arithmo psifiwn
                # sto duadiko systima. Gia paradeigma to 0.1. Tha paroume
                # 0.2x2 = 0.4 katopin 0.4x2 = 0.8, meta 0.8x2 = 1.6,
                # 0.6x2 = 1.2 opote 0.2x2 =0.4 opote exoume pali epanalipsi
                # Gia to logo ayto mporoume na thesoume posa dekadika psifia
                # theloume na exei o duadikos arithmos. Estw loipn k_digits

                
		# Find next bit in fraction 
                dekadiko_tmima *= 2
                duadiko_psifio = int(dekadiko_tmima)

                if duadiko_psifio == 1 : 
                        dekadiko_tmima -= duadiko_psifio
                        duadikos += '1'
                else:
                        duadikos += '0'
                k_digits -= 1

        return duadikos
#=================
# Kurio programma
#=================
num = float(input("Dwse ena dekadiko arithmo: "))
akriveia_psifiwn = 7
#... Klisi tis sunartisis metatropis mesa sto format
print("O arithmos {:10.5f} apeikonizetai sto duadiko sustima ws {:s}".\
      format(num,decimalToBinary(num,akriveia_psifiwn)))

