#!/usr/bin/python3

from numpy import pi, sqrt, abs
nterms = int(input("Give the number of terms in the sum for pi: "))

Leibniz_error = []
Euler_error = []
for i in range(nterms):
    Leibniz_error += [0]
    Euler_error += [0]

#Leibniz approximation
sum1 = 0
for k in range(nterms):
    sum1 += 1.0/((4*k + 1) * (4*k + 3))
    Leibniz_error[k] = pi - 8*sum1
sum1 *= 8
final_Leibniz_error = abs(pi - sum1)
print("Leibniz: ", final_Leibniz_error)

# Euler approximation
sum2 = 0
for k in range(1,nterms+1):
    sum2 += 1.0/k**2
    Euler_error[k-1] = pi - sqrt(6*sum2)
sum2 *= 6
sum2 = sqrt(sum2)
final_Euler_error = abs(pi - sum2)
print("Euler: ", final_Euler_error)

import matplotlib.pyplot as plt
terms = range(nterms)
plt.plot(terms,Leibniz_error,'b-')
plt.plot(terms,Euler_error,'r-')
plt.xlabel('Nterms')
plt.ylabel('Error with Leibniz(blue) and Euler(red)')
plt.show()
