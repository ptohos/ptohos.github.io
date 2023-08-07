#!/usr/bin/python3


def readme(filename):
    x = []
    y = []
    infile = open(filename, 'r')
    for line in infile:
        if line.startswith("#"):
            continue
        xi, yi = line.split()
        pos = xi.find("=")               # Briskoume ti thesi tou =
        xi = float( xi[ (pos+1): ] )     # kai pernoume to tmima tou string
        pos = yi.find("=")               # meta to = ews to telos tou
        yi = float( yi[ (pos+1): ] )
        x += [xi]
        y += [yi]
        # Diaforetikos tropos
        '''
        words = line.split()         # Pernoume mia lista words
        xi = words[0].split('=')[1]  # Eksetazoume to 1 stoixeio (words[0])
                                     # kai to kanoume split me basi to "="
                                     # Ayto epistrefei mia nea list
                                     # words[0].split('=') apo tin
                                     # opoia pernoume to 2 stoixeio
                                     # words[0].split('=')[1]
        yi = words[1].split('=')[1]  # Omoia me prin
        '''
        # Enas akoma tropos:
        '''
        xi = words[0][2:]
        yi = words[1][2:]
        x.append(float(xi))
        y.append(float(yi))
        '''
    return x, y

print(60*('-'))
print("| To programma anamenei na tou dothei to onoma enos file\n"
      "| to opoio periexei tis grammes twn dedomenwn opws dinontai\n"\
      "| ekfwnisi tis askisis")
print(60*('-'))
inpfile = input("Give the file name: ")

x,y = readme(inpfile)
for j in range(len(x)):
    print("%5.4f  %6.5f"%(x[j],y[j]))

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()
