#!/usr/bin/python3

I = input("Dwste mia timi gia tin akeraia metavliti I = ")
I = int(I)     # Metatropi se int apo string

J = input("Dwste mia timi gia tin akeraia metavliti J = ")
J = int(J)

A = float(input("Dwste mia pragmatiki metavliti A = "))
B = float(input("Dwste mia pragmatiki metavliti B = "))
C = float(input("Dwste mia pragmatiki metavliti C = "))
D = float(input("Dwste mia pragmatiki metavliti D = "))


print()

print(" To apotelesma tis ektypwsis ")
print(" ============================")
print(" Dwsate duo akeraies metavlites me times:")
print(" I = ", I, " J = ", J)
print(" Dwsate episis tessereis float metavlites me times:")
print(" A = ", A, " B = ", B, " C = ", C, " D = ", D)

print("==========================")
print(" Merikoi upologismoi twra:")


# Tha typwsoume ta apotelesmata

print()
print(" Perissotera apotelesmata")
print("=========================")
print("To apotelesma z = (A + B)/(C+D) einai: ", (A+B)/(C+D))
print("To apotelesma z = A + B/(C+D) einai: ", A+B/(C+D))
print("To apotelesma z = (A + B)/C+D einai: ", (A+B)/C+D)
print("To apotelesma k = I/J einai: ", I/J)
print("To apotelesma z = 4**(I/J) einai: ", 4**(I/J))

#=======================
quit()
