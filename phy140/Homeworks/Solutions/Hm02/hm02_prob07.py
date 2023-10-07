#!/usr/bin/python3

import numpy as np
import matplotlib as plot

# Metatropi enos arithmou apo to duadiko systima sto dekadiko 

def binaryToDecimal(n):
        num = n
        dec_value = 0

        base = 1   # 2^0 basi systimatos arithimisis

        temp = num
        while(temp):
                # Eyresi tou teleutaiou psifiou tou duadikou arithmou.
                # Diairoume me to 10. To ypoloipo tha einai 0 i 1
                # Epomenws tha prepei na pollaplasiasoume ayto to ypoloipo
                # me tin dinami tou 2^pos opou pos i thesi tou psifiou.
                # Meta tin diairesi gia tin euresi tou psifiou tha prepei
                # na ananewsoume ton arithmo me to piliko tis diairesis
                # me to 10. Etsi tha exoume enan neo duadiko arithmo kai
                # parallila tha ayksisoume ton ektheti tis dunamis tou 2
                # afou tha exoume proxwrisei pros ta aristera
                # Gia paradeigma o arithmos 10101. Stin prwti diairesi (thesi 0)
                # me to 10 to upoloipo tha einai 1 kai to pikiko 1010
                # 10101/10=1010. Etsi last_digit = 1, temp=1010 dec_value=1
                # Stin epomeni epanalipsi tha exoume (thesi 1)
                # temp = 1010/10 = 101, last_digit=0  kai dec_value = 1+0*2^1
                # Stin epomeni epanalipsi tha exoune (thesi 2):
                # temp = 101/10 = 10, last_digit=1 kai dec_value = 1+1*2^2=5
                # Stin epomeni epanalipsi tha exoume (thesi 3)
                # temp = 10/10 = 1, last_digit=0 kai dec_value= 5+0*2^3 = 5
                # Stin teleutaia epanalipsi (thesi 4)
                # temp = 1/10 = 0, last_digit=1 kai dec_value= 5+1*2^4 = 21
                # Epomenws o dekadikos tou duadikou arithmou 1010 einai to 21

                last_digit = temp % 10     # Ypoloipo tis diairesis tou n me 10
                temp = int(temp / 10)      # Piliko tis diairesis
		
                dec_value += last_digit * base
                base = base * 2    # H nea basi
        return dec_value

num = 10101
string1=str(num)  # Metatropi tou duadikou se string gia typwma
print("O duadikos arithmos {:s} antistoixei ston arithmo {:d} tou dekadikou "\
      "systimatos".format(string1,binaryToDecimal(num)))

#===============
#...2os tropos
#===============
'''
 Mporoume na metatrepsoume ton duadiko se string kai
 na diavasoume 1 pros ena tous arithmous ws characters
 Apla xreiazetai na metatrepoume tous characters autous
 se numbers gia tous upologismous
'''
string1 = str(num)
decnum = 0
pos = 0
for let in string1:
        decnum += int(let)*2**pos
        pos += 1
print('\n',50*('='),'\n \t\t 2os tropos with string\n',50*('='))
print("O duadikos arithmos {:s} antistoixei ston arithmo {:d} tou dekadikou "\
      "systimatos".format(string1,binaryToDecimal(num)))
