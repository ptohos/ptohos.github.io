#!/usr/bin/python3

''' Oloklirwsi se duo diastaseis mia sunartisis f(x,y)
    me tin methodo tou endiamesou simeiou. 
    1) Parousiazetai o tropos lusis eite me diplo loop 
    gia to athroisma ws pros x kai y. 
    2) me ton orismo boithitikis sunartisis gia to 
    oloklirwma ws pros ti mia metavlili kai katopin 
    oloklirwsi aytis tis sunartisis
    3) Elegxos kai me to apotelesma tis analytikis lusis
    
    Snartisi f(x,y) = 5x + 8y  x sto [-2,5] kai y sto [0,4]'''


def midpoint_double1(f, a, b, c, d, nx, ny):
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

def midpoint(f, a, b, n):
    ''' H geniki sinartisi gia to endiameso simeio'''
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

def midpoint_double2(f, a, b, c, d, nx, ny):
    ''' Xrisi endiamesis sinartisis '''
    def g(x):
        return midpoint(lambda y: f(x, y), c, d, ny)

    return midpoint(g, a, b, nx)

def test_midpoint_double():
    ''' Elegxos oti mia grammiki synartisi oloklirwnetai akribws.'''
    def f(x, y):
        return 5*x + 8*y

    a = -2;  b = 5;  c = 0;  d = 4

    import sympy
    
    x, y = sympy.symbols('x  y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    
    # Test three cases: nx < ny, nx = ny, nx > ny
    
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed1 = midpoint_double1(f, a, b, c, d, nx, ny)
        I_computed2 = midpoint_double2(f, a, b, c, d, nx, ny)
        print(40*'=')
        print('\t nx =%2d  ny=%2s'%(nx,ny))
        print(40*'=')
        print('Expected integral value  =%.15f'%I_expected)
        print('Integral with double sum =%.15f'%I_computed1)
        print('Integral with interm. function =%.15f'%I_computed2)
        print('Difference of analytical - expect1 ',abs(I_computed1 - I_expected))
        print('Difference of analytical - expect2 ',abs(I_computed2 - I_expected))

test_midpoint_double()

