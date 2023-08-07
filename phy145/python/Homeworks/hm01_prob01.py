#!/usr/bin/python3

import numpy as np

x0 = float(input("Give the initial position "))
v0 = float(input("Give the initial velocity "))
accel = float(input("Give the acceleration "))

time = 0
dt = 0.01
x = x0
v = v0

while x >= 0.0 or time == 0 :
    Tol_step = time
    x = x0 + v0*time + 0.5* accel * time**2
    v = v0 + accel * time
    time = time + dt 

#Ypologismos tou xronou kinisis theoritika
#  x=0 kai x0 = 0 => Tol = [-v0 - sqrt(v0*v0 - 2*accel*x0)]/accel
Tol_theory =  (-v0 - np.sqrt(v0*v0 - 2*accel*x0))/accel
print("O xronos kinisis einai [ypologistika]:%.3f"%(Tol_step))
print("O xronos kinisis einai [theoritika]:%.3f"%(Tol_theory))
quit()
