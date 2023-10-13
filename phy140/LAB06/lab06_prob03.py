#!/usr/bin/python3

import numpy as np

# Anagnwsi dedomenwn me open kai apothikeusi me analogo tropo
# H anagnwsi perigrafetai stin askisi2 tou Lab06

inpfile = 'FreqData.txt'
file_in = open(inpfile,'r')
f = []
a = []
da = []
for line in file_in:
    cline = line.strip()             # remove spaces
    if not(cline[0:1].isnumeric()) : # skip line if there are any characters
        continue                     # and no pure numbers
    data = cline.split()             # read-in numbers in a list data
    f += [float(data[0])]            # take the individual elements of the list
    a += [float(data[1])]            # convert them to float and add them to 
    da+= [float(data[2])]             # the lists
file_in.close()
print(" %6s %12s %12s" % ("frequency(Hz)","amplitude(mm)", "amp error(mm)"))
for i in range( 0, np.size(f) ) :
    print(" %12.4f   %10.2f  %10.2f" % (float(f[i]),float(a[i]),float(da[i])))
    
outfile = "lab06_prob03.txt"
file_out = open(outfile,'w')
info  = " Data: 06 - 10 - 2022"
info += "\n Data taken by Andria and Marios"
info += "\n Frequency(Hz) amplitude(mm) amp error(mm)"    
file_out.write(info)
for i in range(len(f)):
    file_out.write("%13.4f %14.2f %10.2f\n"%(f[i],a[i],da[i]))
file_out.close()
