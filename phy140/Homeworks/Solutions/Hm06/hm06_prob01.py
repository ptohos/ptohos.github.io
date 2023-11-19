#!/usr/bin/python3
'''
   Eyresi twn timwn tis aktinas kai ypsous enos kwnou
   pou elaxistopoioun tis epifaneies tis basis kai pleuras
   gia stathero ogko

   Apo ti sxesi V = pi*R^2*H=>R=sqrt[3V/(pi*H)]
   kai antikathistoume sti sxesi tou emvadou
   S=pi*R*L = pi*sqrt(R^2+H^2)*sqrt[3V/(pi*H)]
   S=pi*sqrt[3V/(pi*H)]*sqrt[3V/(pi*H) + H^2]=>
   S=sqrt[3V*pi/H]*sqrt[3V/(pi*H) + H^2] =>
   S=sqrt[9V^2/H^2 + 3V*H*pi]
   Tha prepei na paragwgisoume ws pros H kai
   na zitisoume na midenizetai wste na broume
   to akrotato.
   H paragwgos ws pros H dinei:
   dS/dH = 1/(2*S) * d/dH (9V^2/H^2 +3V*H*pi)
   kai pernoume h^3 = 288/pi = 4.51cm
   kai analoga R = 3.19cm
'''

import numpy as np

def sympy_func(Vol):
    from sympy import symbols, sqrt, pi, diff
    from sympy.utilities.lambdify import lambdify
    R, H, V = symbols('R H V')
    V = Vol
    S = sqrt(9*V*V/(H*H) + 3*V*H*pi)
    d1SdH = diff(S,H,1)
    d2SdH = diff(S,H,2)
    #
    d1f=lambdify(H,d1SdH,'numpy')
    d2f=lambdify(H,d2SdH,'numpy')
    #
    return d1f, d2f

def Newton(d1f,d2f,xl,eps,nit_mx):
    x = xl
    f_x = d1f(x)
    it_counter = 0
    while np.abs(f_x) > eps and it_counter < nit_mx:
        try:
            x = x - f_x/d2f(x) 
        except ZeroDivisionError:
            print('Error! - denominator is zero for x = ',x)
            sys.exit(1)
        f_x = d1f(x)
        it_counter += 1
    if abs(f_x) > eps:
        it_counter = -1
    return x, it_counter

def main():
    Vol = float(input("What is the Volume of the cone ?"))
    x0  = float(input("Initital value for x = "))
    eps = 1E-6
    n = 100
    d1f, d2f = sympy_func(Vol)
    root, ic  = Newton(d1f,d2f,x0,eps,n)
    print("The minimal conical surface is for h = ",root)
    print("The radius is then R = ",np.sqrt(3*Vol/(np.pi*root)))
    
main()

    
