#!/usr/bin/python3

#=====================================
# Ypologismos pragmatikis rizas 
# enos polionumou 3ou bathmou
#   x^3 + ax^2 + bx + c = 0
#
#  H riza einai: x0 = W + Z - a/3
#  opou
#      W = (-q/2 + sqrt(R))^(1/3)
#      Z = (-q/2 + sqrt(R))^(1/3)
#      R = p^3/27 + q^2/4
#      p = -a^2/3 + b
#      q = 2*a^3/27 - a*b/3 + c
#==========================================
# Dokimi gia a=3, b=8 kai c=24 dinei x0=-3
#==========================================

import numpy as np

A = float(input('Enter the coefficient of the x^2 term '))
B = float(input('Enter the coefficient of the x term '))
C = float(input('Enter the constant term '))

#
p = -A*A/3. + B
q = 2*A*A*A/27. - A*B/3. + C
R = p*p*p/27 + q*q/4
#
sqrt_R = np.sqrt(max(0,R))
half_q = -q/2.
#
Wsq = half_q + sqrt_R
Zsq = half_q - sqrt_R
#
'''
An oi 2 proigoumenes posotites einai arnitikes tote den mporei
na ypologistei i kiviki riza dinontas ws apotelesma migadiko arithmo
eite pernontas ti sunartisi (x)**(1/3.) eite pow(x,1/3.)
Wstoso i kibiki riza enos arithmou orizetai mathimatika kai einai 
pragmatikos arithmos. 
Gia na lusoume to provlima, tha prepei na kratisoume to prosimo tis 
uporizis posotitas kai sti sunexeia na upologisoume tin kuviki riza
tis apolytis timis tis uporizis posotitas kai to apotelesma na to 
pol/soume me to prosimo pou exoume kratisei. 
'''
prosimo = Wsq/abs(Wsq)
W = prosimo*(abs(Wsq))**(1./3.)
prosimo = Zsq/abs(Zsq)
Z = prosimo*(abs(Zsq))**(1./3.)
#
# H pragmatiki riza einai:
x0 = W + Z - A/3.
print('H pragmatiki riza tou poluwnumou x^3 + %d*x^2 + %d*x + %d = 0'%(A,B,C)) 
print('einai x0 = %6.2f'%x0)

quit()
