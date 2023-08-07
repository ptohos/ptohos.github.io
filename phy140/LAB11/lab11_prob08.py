#!/usr/bin/python3
''' Oloklirwsi se duo diastaseis mia sunartisis f(x,y)
    me tin methodo tou endiamesou simeiou. 
    1) Parousiazetai o tropos lusis eite me diplo loop 
    gia to athroisma ws pros x kai y. 
    2) Me ti methodo MC endiamesis timis 
    3) Elegxos kai me to apotelesma tis analytikis lusis
    
    Synartisi f(x,y) = 5x + 8y  x sto [-2,5] kai y sto [0,4]'''

from random import seed, random


def Integrate_MC_ave(f,a,b,c,d):
    seed(1234567)
    ntries = 1000000
    sum = 0
    for itries in range(ntries):
        xr = a + (b-a)*random()
        yr = c + (d-c)*random()
        sum +=f(xr,yr)
    integral = (b-a)*(d-c)*sum/ntries
    return integral
    
def midpoint_double(f, a, b, c, d, nx, ny):
    '''Xrisi diplou athroismatos'''
    hx = (b - a)/float(nx)
    hy = (d - c)/float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + hx/2 + i*hx
            yj = c + hy/2 + j*hy
            I += hx*hy*f(xi, yj)
    return I

def test_double_integral():
    ''' Elegxos oti mia grammiki synartisi oloklirwnetai akribws.'''
    def f(x, y):
        return 5*x + 8*y

    a = -2;  b = 5;  c = 0;  d = 4

    import sympy
    
    x, y = sympy.symbols('x  y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    
    # Test three cases: nx < ny, nx = ny, nx > ny
    
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed = midpoint_double(f, a, b, c, d, nx, ny)
        print(40*'=')
        print('\t nx =%2d  ny=%2s'%(nx,ny))
        print(40*'=')
        print('Expected integral value  =%.15f'%I_expected)
        print('Integral with double sum =%.15f'%I_computed)
        print('Difference of analytical - expect1 ',abs(I_computed - I_expected))
    print(40*'=')
    I_MCcomputed = Integrate_MC_ave(f, a, b, c, d)
    print('Integral with Monte Carlo =%.15f'%I_MCcomputed)
    print('Difference of analytical - MCintegral ',abs(I_MCcomputed - I_expected))

        
test_double_integral()

