#!/usr/bin/python3

# Lista 2 diastasewn me 5 grammes kai 2 stiles
A=[ [1,2], [3,4], [5,6], [7,8], [9,10] ]

A[2]           # Tha typwsei to 3o stoixeio, diladi [5,6]
A[2:4]         # Tha typwsei [5,6],[7,8],[9,10]
A[2][1]        # Tha typwsei to stoixeio tis 2-is grammis kai 1-is stilis to 6
A[2][2]        # Tha dwsei sfalma giati einai to stoixeio 2-is grqammis kai
               # 2-is stilis pou den uparxei
A[2]=[1,1]     # Allagi tou 3ou stoixeiou tis listas apo [5,6] se [1,1]
print(A)
A[3][0] = 0    # Allagi tou stoixeiou tis 4-is grammis kai 1-is stilis apo 7->0
print(A)
A.append([16,4])
print(A)

'''
Tha mporousame na to kanoume kai ws
'''
A +=[[25,5]]  # Prosoxi oti xrisimopoioume 2 agkules. H 1-i gia ton orismo tis
              # list kai i 2-i gia to stoixeio pou einai episis list
print(A)



                        
