#!/usr/bin/python3

import numpy as np

inpfile=input('Give the name of the file ')
file2read = open(inpfile,'r')
A = []
nDoubles = 0
count = 0
for lines in file2read:
    DblFound = False
    count +=1
    try:
        numb = int(lines.strip())
    except:
        continue

    for ii in range(len(A)):       # Elegxos an o arithmos prouparxei
        if numb == A[ii] :
            if nDoubles == 0 : print(20*'=')

            print('To stoixeio %d toy file me arithmo %d exei\n'
                  'idi kataxwrethei sti thesi %d'%(count,numb,ii))
            nDoubles +=1
            DblFound = True
            break                 # Den kratame to stoixeio
        
    if (not DblFound):  A += [numb]    # Apothikeusi tou arithmou

file2read.close()
print(40*'=')
print(' Diabastikan synolika %d stoixeia '%count)
print(' Sumplirwthikan %d theseis tou pinaka A'%len(A))
print(' Vrethikan %d doublicate records'%nDoubles)
print(40*'=')

WantedSum = int(input('Dwste to epithumito athroisma dyo orwn [75] '))

print('Ta zeugi twn stoixeiwn me athroisma %d einai:'%WantedSum)
for jj in range(len(A)-1):         # Eksetazoume ta stoixeia tou pinaka A
    for kk in range(jj+1,len(A)):   # se zeugos me ta stoixeia tou pinaka pou
        thesum=A[jj]+A[kk]          # vriskontai stis epomenes theeseis
        if thesum == WantedSum:     # Efoson theloume zeygi, to ekswteriko loop
            print(' (%d,%d)'%(A[jj],A[kk])) # pigainei mexri N-1 wste to inner
                                    # loop na kalypsei tin teleytaia thesi
