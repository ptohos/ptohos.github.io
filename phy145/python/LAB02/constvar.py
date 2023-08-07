#!/usr/bin/python3

I = input("Dwste mia timi gia tin akeraia metavliti I = ")
I = int(I)     # Metatropi se int apo string

J = input("Dwste mia timi gia tin akeraia metavliti J = ")
J = int(J)

K = int(input("Dwste mia timi gia tin akeraia metavliti K = ")) # aytomati metatropi se int

X = float(input("Dwste mia pragmatiki metavliti X = "))
Y = float(input("Dwste mia pragmatiki metavliti Y = "))
Z = float(input("Dwste mia pragmatiki metavliti Z = "))
S = input("Dwste mia string metavliti S = [10 char max] ")
T = input("Dwste mia string metavliti T = ]10 char max] ")

print()

print(" To apotelesma tis ektypwsis ")
print(" ============================")
print(" Dwsate treis akeraies metavlites me times:")
print(" I = ", I, " J = ", J, " K = ", K)
print(" Dwsate episis treis float metavlites me times:")
print(" X = ", X, " Y = ", Y, " Z = ", Z)
print(" Orisate episis 2 metavlites xaraktirwn me times:")
print(" S = ", S, " T = ", T)

print("==========================")
print(" Merikoi upologismoi twra:")
index1 = 2*I
index2 = 3*I - 4*J
index3 = 5*I - 3*J + 4*K
time = X**2
vel = (X+Y)/2.0
acceleration = 5*(X*Y + Y*Z)
line1 = S+T

# Tha typwsoume ta apotelesmata

print()
print(" Perissotera apotelesmata")
print("=========================")
print("Oi times twn metavlitwn index1, index2, index3 einai:")
print(index1,index2, index3)
print()
print("Enw oi times twn metavlitwn time, vel kai acceleration einai:")
print(time, vel, acceleration)
print("Telos i metavliti string line1 exei timi:")
print(line1)

#=======================
quit()
