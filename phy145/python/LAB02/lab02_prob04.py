#!/usr/bin/python3

# Read two temperature
TempC = float(input("Give me the temperature in Celcius "))
TempF = (9./5.)*TempC + 32    # Kalo na xrisimopoioume float gia diairesi 
                              # duo akeraiwn gia na apofugoume apokopi dekadikwn
                              # poy symbainei stin python2 kai alles glwsses
                              # programmatismou

print("H thermokrasia",TempC,"C antistoixei se",TempF,"F")

# Metatropi tis F se C
TempC = (5./9.)*(TempF - 32)
print("H thermokrasia",TempF,"F antistoixei se",TempC,"C")

quit()
