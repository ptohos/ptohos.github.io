#!/usr/bin/python3

nrows = int(input("Give the number of rows "))
ncols = int(input("Give the number of columns "))

A=[]      # Dimiourgia mias kenis listas

for i in range(nrows):       # loop ws pros tis grammes pou theloume
    rowmat = []              # Dimiourgia mias neas listas gia na kratisoume 
                             # ta stoixeia tis kathe grammis tou A
    for j in range(ncols):   # loop ws pros ta stoixeia tis grammis, ana stili
        if i == 0 or i == nrows-1:  # Ta stoixeia tis 1-is kai teleytaias grammis
            numb = 4         # einai 4
        else:
            if j==0 or j == ncols-1:  # 1-i kai teleutaias stili
                numb = 4     # einai 4
            else:
                numb = 2     # Ola ta upoloipa tha einai 2
        rowmat +=[numb]      # Eisagwgi twn arithmwn stin i-th grammi tou A
    A +=[rowmat]             # Eisagwgi sti list A to stoixeio i pou einai 
                             # list. Ara tha exoume list of lists.
                             # Tha mporousame na grapsoume A.append(rowmat).
                             # Prosoxi oti an valoume apla A+=rowmat tha
                             # prostethoun ta stoixeia tis listas rowmat san
                             # na anikan se mia kai mono grammi kai o A tha
                             # itan 1-D kai oxi 2-D
'''
Ektypwsi tis listas
'''
for i in range(nrows):
    for j in range(ncols):
        print("%4d"%(A[i][j]),end=' ')
    print()

   
