def func(x):
    from numpy import exp, cos
    return exp(-x**2)*cos(4*x)

def brute_force_optimizer(func, xmin, xmax, nsteps):
    dx = (xmax - xmin)/nsteps       # vima dx
    x = [xmin + i*dx for i in range(nsteps+1)]
    y = list(map(func,x))
    # maxima kai minima kratoun tous deiktes twn thesewn
    # pou antistoixoun sta (topika) akrotata (maxima i minima)
    minima = []
    maxima = []
    for i in range(1, nsteps-1):        # Eswterika simeia mono
        if y[i-1] < y[i] > y[i+1]:
            maxima.append(i)       # Apothikeusi twn thesewn twn stoixeiwn
                                   # tis listas poy einai megista
        if y[i-1] > y[i] < y[i+1]:
            minima.append(i)
    # Euresi tou megistou apo ola ta megista me ti methodo max gia listes
    # Dimiourgia mias listas me list comprehension me tis megistes
    # times tis sinartisis opws vrethikan 
    y_max_inner = max([y[i] for i in maxima])

    # Euresi tou elaxistou apo ola ta elaxista 
    y_min_inner = min([y[i] for i in minima])

    # Eksetasi gia to an to 1o i teleytaio simeio tis sunartisis
    # einai megalytero i mikrotero tou olikou megistou/elaxistou
    if y[0] > y_max_inner:
        maxima.append(0)          # An to 1o simeio tis sinartisis einai
                                  # megalytero apo to mexri twra megisto
                                  # apothikeuoume tin thesi sti lista twn
                                  # thesewn me ta megista
    if y[len(x)-1] > y_max_inner: # Analoga gia to teleytaio simeio tis 
        maxima.append(len(x)-1)   # sunartisis
    if y[0] < y_min_inner:
        minima.append(0)
    if y[len(x)-1] < y_min_inner:
        minima.append(len(x)-1)

    '''
    # Epistrofi mias listas ta stoixeia tis opoias
    # einai oi suntetagmenes twn megistwn se morfi
    # [ [xmax1,ymax1],
    #   [xmax2,ymax2], ...]
    '''
    return [(x[i], y[i]) for i in maxima], \
           [(x[i], y[i]) for i in minima]

def demo():
    minima, maxima = brute_force_optimizer(func, 0, 4, 1000)
    print('Minima:', minima)
    print('Maxima:', maxima)

if __name__ == '__main__':
    demo()
    
