#!/usr/bin/python3

from numpy import linspace, zeros, sqrt, log

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

def adaptive_integration(f, a, b, eps, method='midpoint'):
    n_limit = 1000000   # Xrisi gia apofugi atermonou loop

    n = 2
    if method == 'trapezoidal':
        integral_n  = trapezoidal(f, a, b, n)
        integral_2n = trapezoidal(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        print('trapezoidal diff: ', diff)
        while (diff > eps) and (n < n_limit):
            integral_n  = trapezoidal(f, a, b, n)
            integral_2n = trapezoidal(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            print('trapezoidal diff: ', diff)
            n *= 2
    elif method == 'midpoint':
        integral_n  = midpoint(f, a, b, n)
        integral_2n = midpoint(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        print('midpoint diff: ', diff)
        while (diff > eps) and (n < n_limit):
            integral_n  = midpoint(f, a, b, n)
            integral_2n = midpoint(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            print('midpoint diff: ', diff)
            n *= 2
    else:
        print('Error - adaptive integration called with unknown par')

    # Elegxos an brethike apodekto n
    if diff <= eps:   # Success
        print('The integral computes to: ', integral_2n)
        return n
    else:
        return -n   # Return negative n to tell "not found"


def main():

    def f(x):
        return x**2
    def g(x):
        return sqrt(x)

    #eps = 1E-1           # Enallagi metaksu twn duo aytwn timwn 
    eps = 1E-10           # epithumitis akriveias
    #a = 0.0
    a = 0.0 + 0.01;       # Metatropi tou katw oriou gia apofugi
    b = 2.0               # provlimatos sugklisis me tin sqrt(x) sunartisi
                          # Sti methodo tou trapeziou/mesou simeiou i apokopi
                          # orwn ginetai stin deuteri paragwgo tis sunartisis
                          # pros oloklirwsi. Sti periptwsi tis sqrt(x) i
                          # 2-i paragwgos apeirizetai arnitika kathw x->0 opote
                          # epanaprosdiorizoume to orio gia na epitheyxthei
                          # sygklisi
    # Arxika tin synartisi f
    n = adaptive_integration(f, a, b, eps, 'midpoint')
    if n > 0:
        print('Sufficient n is: %d' % (n))
    else:
        print('No n was found in %d iterations' % (n_limit))

    n = adaptive_integration(f, a, b, eps, 'trapezoidal')
    if n > 0:
        print('Sufficient n is: %d' % (n))
    else:
        print('No n was found in %d iterations' % (n_limit))

    # Twra tin sunartisi g
    n = adaptive_integration(g, a, b, eps, 'midpoint')
    if n > 0:
        print('Sufficient n is: %d' % (n) )
    else:
        print('No n was found in %d iterations' % (n_limit))

    n = adaptive_integration(g, a, b, eps, 'trapezoidal')
    if n > 0:
        print ('Sufficient n is: %d' % (n))
    else:
        print ('No n was found in %d iterations' % (n_limit))

    # Plot gia midpoint kai trapezoidal
    eps = linspace(1E-1,10E-10,10)
    n_m = zeros(len(eps))
    n_t = zeros(len(eps))
    for i in range(len(n_m)):
        n_m[i] = adaptive_integration(g, a, b, eps[i], 'midpoint')
        n_t[i] = adaptive_integration(g, a, b, eps[i], 'trapezoidal')

    import matplotlib.pyplot as plt
    plt.figure(figsize=(7,5))
    plt.plot(log(eps),n_m,'b-',label='midpoint')
    plt.plot(log(eps),n_t,'r-',label='trapezoidal')
    plt.xlabel('log(eps)')
    plt.ylabel('n for midpoint (blue) and trapezoidal (red)')
    plt.xlim(-25,0)
    plt.ylim(0,140000)
    plt.grid(True)
    plt.show()
    print(n)
    print(eps)

main()


'''
Apo to plot toy n sunartisei tou log(eps) toso gia ti methodo tou mesou simeiou
oso kai ti methodo tou trapeziou, paratiroume oti gia pio aystires times tis 
epithymitis akriveias, i diafora twn apotelesmatwn metaksu twn duo methodwn 
auksanei. Gia dedomeni timi akriveias, i methodos toy mesou simeiou dinei 
apotelesma me tin epithumiti akriveia xrisimopoiontaw ligotera upodiastimata
se sxesi me ti methodo toy trapeziou. Ayto einai anamenomeno efoson i methodos 
toy mesou simeiou parolo pou einai idias taksis prosegkisis me ti methodo tou 
trapeziou einai perissotero akribis logw tou orou sti 2-i paragwgo. 
'''  
