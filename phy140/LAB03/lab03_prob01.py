#!/usr/bin/python3

# dimiourgia enos 1-D numpy array a me plithos 20 stoixeiwn
a = [1,2,12,4,5,34,5,7,8,12,-1,9,11,10,15,78,32,23,29,17,14,13,20]

a[:]               # Ektupwsi olwn to stoixeiwn tou array a apo to perissotero
                   # aristera ews to perissotero deksia
a[::]              # Opws kai i proigoumeni entoli mono pou stin prokeimeni
                   # periptwsi vazoume kai tin epilogi tou vimatos gia
                   # tin prosvasi sta stoixeia tou array
a[5:15]            # Ektupwsi twn stoixeiwn tou array a ksekinontas apo ayto
                   # poy vrisketai sti thesi 5 (einai to 6 se plithos stoixeio)
                   # ews kai to stoixeio sti thesi 14. Euros thesewn epomenws
                   # [5,15) ή [5,14]
a[5:15:3]          # Opws kai i proigoumeni entoli alla me vima prosbasis 3
                   # Tha tupwsei ta stoixeia stis theseis 5,8,11,14.
                   # Oi times tha einai a[5]->5, a[8]->8, a[11]->11, a[14]->14
a[5::]             # Opws kai proigoumenws tha ektupwsei oles tis times tou
                   # array A ksekinontas apo to stoixeio sti thesi 5 ews to
                   # telos tou array me vima 1.
a[:5:]             # Ektypwsi apo to stoixeio sti thesi 0 ews to stoixeio sti
                   # thesi 4 me vima prosvasis 1
a[::5]             # Ektypwsi apo to stoixeio sti thesi 0 ews to telos tou
                   # array me vima prosvasis 5. Diladi tha ektypwsei mono ta
                   # stoixei a[0],a[5],a[10],a[15]. To a[20] den tha ektypwthei
                   # giati den einai meros toy array a o opoio exei stoixeia
                   # apo 0 ews 19

'''
Gia na paroume tis perittes theseis tis listas a tha kanoume
'''
a[1::2]            # Ektypwsi apo to stoixeio sti thesi 1 ews to telos me vima 2

'''
To mikos tou lista a
'''
n = len(a)     # 1os tropos ws methodos tis numpy
print("to mikos tis listas a einai: ",n)

'''
Gia na prosthesoume epipleon stoixeia se enan numpy pinaka
xrisimopoioume tin methodo append.
Tha prepei na dwsoume se ena tuple ta stoixeia pou theloume na eisaksoume.
'''
a.append(30)     # Apla eisagei ta stoixeia 30,40,50 kai to typwnei
a.append(40)     # Apla eisagei ta stoixeia 30,40,50 kai to typwnei
a.append(50)     # Apla eisagei ta stoixeia 30,40,50 kai to typwnei
print(a)

'''
Enas 2os tropos gia na prosthesoume ta stoixeia einai με ti methodo extend
'''
a +=[60,70,80]   # Prosthesi sti list a mias neas list me stoixeia [30,40,50]
print(a)
'''
Enas 3os tropos gia na prosthesoume ta stoixeia einai με ti methodo extend
'''
a.extend((100,110,120)) # Tha prepei na perasoyme ta stoixeia ws tuple
print(a)


