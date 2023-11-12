#!/usr/bin/python3

import sympy as sp

x = sp.Symbol('x')
cnst = 0
f   = sp.tanh(x)                          # orismos tis synartisis
eq  = sp.Eq(f,cnst)                          # tanh(x) = 0
sol = list(sp.solveset(eq,x,sp.S.Reals))  # zitoume mono Real solutions
if len(sol) != 0 :
    print("H lysi tis eksiswsis %s = %.1f einai: "%(f,cnst),sol[0])
else:
    print("Den brethike lusi gia tin eksiswsi %s = %.1f"%(f,cnst))
quit()
