#!/usr/bin/python3

# Read two numbers
Numb1 = float(input("Give me the first number "))
Numb2 = float(input("Give me the second number "))

Diff = Numb1**2 - Numb2**2

print("Dothikan duo arithmoi:", Numb1,"kai", Numb2)
print("Ta tetragwna tous einai: N1^2 =",Numb1**2, "N2^2 =",Numb2**2)
print("H diafora twn tetragwnwn tous einai: ",Diff)


# To idio provlima me ti xrisi listas
Numbs = []                           # Dimiourgia mias kenis listas
for j in range(1,3):                 # Loop gia tin eisagwgi twn arithmwn
    print("Give me number",j)
    anum = float(input())            # Den xreiazetai kapoio sxolio
    Numbs.append(anum)               # eisagwgi tou arithmou stin lista

Diff = Numbs[0]**2 - Numbs[1]**2    
print("Dothikan duo arithmoi:", Numbs[0],"kai", Numbs[1])
print("Ta tetragwna tous einai: N1^2 =",Numbs[0]**2, "N2^2 =",Numbs[1]**2)
print("H diafora twn tetragwnwn tous einai: ",Diff)

