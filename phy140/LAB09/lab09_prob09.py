#!/usr/bin/python3

import sympy as sp

x = sp.Symbol('x')
const = 0
f   = x**3 - 6*x**2 + 9*x                 # orismos tis synartisis
eq  = sp.Eq(f,const)                      # x**3 - 6*x**2 + 9*x = 0
sol = list(sp.solveset(eq,x,sp.S.Reals))  # i solveset epistrefei mia lusi mono
Nsol = len(sol)
comm="Luseis tis eksiswsis %s = %.1f einai "+ Nsol * " %.1f"
print(comm%(f,const,*sol))

sols = [sp.rootof(eq,x,i) for i in range(3)] # oles oi luseis - 3 afou exoume
                                             # poluonumo 30-is taksis
Nsols = len(sols)
comm="Yparxoun %d real luseis gia tin %s = %.1f kai einai: " + Nsols * " %.1f"
print(comm%(Nsols,f,const,*sols))

quit()
