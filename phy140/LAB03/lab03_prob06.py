#!/usr/bin/python3

'''
  O xeiroteros tropos
'''
Celcius=[]     # Dimiourgia mias adeias listas
Fahrenheit=[]  # Dimiourgia mias adeias listas 
i=0
Fahrenheit.append(float(input("Thermokrasia 1: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 2: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 3: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 4: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 5: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 6: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 7: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 8: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 9: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 
i+=1
Fahrenheit.append(float(input("Thermokrasia 10: ")))
Celcius.append(Fahrenheit[i]*5/9 -5*32/9) 

print("Oi thermokrasies se Fahrenheit")
print(Fahrenheit)
print("Oi thermokrasies se Celcius")
print(Celcius)


'''
       Kaluteros tropos
Metatropi tis list Fahreinheit se numpy array kai xrisi vectorization
'''
import numpy as np
Fahrenheit2 = np.array(Fahrenheit)
Celcius2 = (Fahrenheit2 - 32)*5/9   # Ektelesi twn praksewn se ola ta stoixeia
                                    # tou array Fahrenheit2

'''
      Eisagwgi twn thermokrasiwn me loop
      kai sxoliwn me format
      kai ektypwsis twn timwn me oti kserete mexri kai tin dialeksi 6
'''

Far = []
Cel = []
i = 1
while (i) :
    print("Eisagwgi thermokrasiwn \n
           Dwste mi arithmitiki timi gia na stamatisete")
    try:
        s = 'Eisagwgi tis %2d-is thermokrasias (F): '%(i)
        Far.append(float(input(s)))
        i +=1
    except:
        print('Diavastikan %2d thermokrasies'%(i) )
        break      # Gia na bgoume apo to while loop 

    
print("Metatropi bathmwn Fahrenheit se Celcius\n %3s %10s"%('(F)','(C)'))
for i in range(len(Far)):
    Cel += [ (Far[i]-32)*5/9 ]    # Dimiourgia list me ti metatropi kai
                                  # prosthesis tis sti list tou Cel
    print('{:6.2f}    {:6.2f}'.format(Far[i],Cel[i]))

'''
 Anti tou loop ws pros ti thesi twn stoixeiwn sti lista Far tha
 mporousame na xrisimooiiisoume apeutheias ta stoixeia
'''
print(" Diaforetika")
print("Metatropi bathmwn Fahrenheit se Celcius\n %3s %10s" % ('(F)','(C)'))
for F in Far:
    C = (F - 32)*5/9         # Edw den kanoume xrisi listas gia to C
    print('{:6.2f}    {:6.2f}'.format(F,C))

