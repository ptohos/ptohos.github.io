#!/usr/bin/python3

inpfile=input('Give the name of the file ')
file2read = open(inpfile,'r')
numbers = []

for lines in file2read:
    try:
        numb = float(lines.strip())
    except:
        continue
    numbers += [numb]

file2read.close()
numbers.sort()      # Taksinomisi se ayksousa seira. Gia fthinousa tha diname
                    # sort(reverse=True)
print('Oi arithmoi einai:')
for ii in range(0,len(numbers),5):
    print(5*'%4.0f'%(numbers[ii+0],numbers[ii+1],numbers[ii+2],numbers[ii+3], numbers[ii+4]))

''' 
Tha mporousame na grapsoume tin parapanw entoli se ligo diaforetiki 
morfi, ekmetaleuomenoi to gegonos oti mporoume na anagkasoume tin entoli 
print na min allaksei grammi. Sunithws se kathe entoli print, oti bazoume 
san orisma akoloytheitai sto telos automata me \n, diladi me allagi grammis.
Mporoyme na apofugoume to \n bazontas to keyword, end=' ', pou simainei oti 
anti gia \n xrisimopoiei space kai epomenws den allazei grammi. 
Etsi tha grafame to parapanw loop ws ekseis:
'''
print(20*'=')
print('Me diaforetiko tropo')
print('Oi arithmoi einai:')
for ii in range(0,len(numbers),5):
    for jj in range(5):
        print('%4.0f'%numbers[ii+jj],end=' ')
    print()    # Ayto xreiazetai wste na allaksoume grammi meta ta 5 noumera
               # pou typwthikan sto proigoumeno jj loop
    


