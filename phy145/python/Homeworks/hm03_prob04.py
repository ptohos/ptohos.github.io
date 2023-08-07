#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def unpack_line(InputLine):
    words = InputLine.split()
    pos = 0
    country=''
    for word in words:
        if pos == 0: 
            if word[0].isdigit():
                indx = int(word)
        else:
            if not word[0].isdigit():
                country += word+" "
            else:
                popul = word.replace(",","")
                
        pos +=1
    return indx, country, popul

Benford = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]   # Default percentage
population_file = open("population.txt",'r')
Digit_Counts = {d:0 for d in "123456789"}     # Dictionary with the digits
                                              # 1,...,9 as labels
total = 0
for line in population_file:
    line = line.strip()
    if line:
        Rank, Country, Population = unpack_line(line)
        print('{:4d} {:20s} {:10d}'.format(Rank, Country, int(Population)))
        first_digit = Population[0]
        Digit_Counts[first_digit] += 1
        total += 1

percents = sorted([(int(digit), count/total) for digit,count in Digit_Counts.items()])

print(' {:5s}  {:10s}  {:6s}'.format('Digit', 'Population', 'Benford'))
xdigi = []
yperc = []
for dig,pcnt in percents:
    print('{:4d} {:10.1f} {:10.1f}'.format(dig, 100*pcnt,Benford[dig-1]))
    xdigi += [dig]
    yperc += [100*pcnt]

xdigi=np.array(xdigi)
yperc=np.array(yperc)
fig, ax = plt.subplots()
width=0.3
ax.bar(xdigi - width/2,yperc,width,label='Measured',color='b')
ax.bar(xdigi + width/2,Benford,width,label='Default',color='g',hatch='/',fill=False)
ax.set_title("Benford distribution using the population of the countries")
ax.set_xlabel("Digits")
ax.set_ylabel("Frequency (%)")
ax.set_xlim(0,10)
ax.set_ylim(0,33)
ax.set_xticks(xdigi)
ax.legend()
fig.tight_layout()
plt.savefig("Benford.pdf")
plt.show()
