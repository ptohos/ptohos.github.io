#!/usr/bin/python3

# Read three numbers
A = float(input("Give me the 1st number "))
B = float(input("Give me the 2nd number "))
C = float(input("Give me the 3rd number "))

# Find the maximum of the 3 numbers
maxnum = A
if B > maxnum:
    maxnum = B
if C > maxnum:
    maxnum = C

print("===================================================")
print("The maximum of the 3 given numbers is",maxnum)

# Taksinomisi kata fthinousa seira
max1 = A      # Ypothetw oti oloi oi arithmoi einai taksinomimenoi me to A
max2 = A
max3 = A 
# An to B einai megalytero apo to megisto tote
# ton topothetw sti thesi tou megistou
if B > max1 :
    max1 = B
else:           # Oi 2 mikroteroi tha einai o B
    max2 = B
    max3 = B

if C  > max1 :   # An o C einai megaluteros apo ton megisto twn A kai B tote
    temp = max1  # mpainei sti megisti thesi kai metatopizontai ta alla 2 pros
    max1 = C     # tis xamiloteres theseis
    max3 = max2
    max2 = temp
elif C > max2:   # Eksetasame prwta me ton megalutero epomenw an erthei edw
                 # o C tha einai mikroteros apo ton yparxonta megisto
    temp = max2
    max2 = C
    max3 = temp
else:            # Diaforetika einai o mikroteros
    max3 = C 
    
print("H taksinomisi twn 3 dedomenwn arithmwn einai:",max1," ",max2," ",max3)

#=============================
# Taksinomisi me xrisi listas
#=============================
print("===================================================")
print("Apotelesmata xrisimopoiontas antikeimeno tupou list")
Numbs = [A, B, C]          # Eisagwgi twn 3 arithmws sti lista
Xnumbs = Numbs             # Antigrafi tis listas se alli lista
maximum = max(Numbs)       # Xrisi ti sinartisis max gia euresi toy megistou
Numbs.sort(reverse=True)   # Taksinomisi se fthinousa seira
                           # H methodos sort allazei ti list
                           # Tha mporousame na xrisimopoiisoume ti methodo
                           # newlist = shorted(Numbs,reverse=True)
                           # pou epitrefei mia taksinomimeni antigrafi tis
                           # listas kai den allazei tin arxiki lista

print("The maximum of the 3 given numbers is",maximum)
print("H taksinomisi twn 3 dedomenwn arithmwn einai:",Numbs)
print("=========")
print("H taksinomisi tis listas me basi ti sunartisi sorted einai")
print(sorted(Xnumbs,reverse=True))  # Default einai taksinomisi auksousa seira
                                    # opote reverse=False
quit()
