#!/usr/bin/python3

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
