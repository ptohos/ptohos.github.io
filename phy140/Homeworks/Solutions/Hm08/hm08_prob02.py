#!/usr/bin/python3

import numpy as np
from random import seed, random

def func(x,y):
    '''Stin periptwsi mporoume na theorisoume oti i sunartisi
       pros oloklirwsi einai f(x,y)=1 giati i g(x,y) kathorizei
       tin perioxi pou eksetazoume gia ton upologismo tou
       oloklirwmatos. To trigwno pou vrisketai sto orthogwnio
       me pleyres [-1,1] x [0, 3]'''
    return 1
  
def g(x, y):
    """Stin periptwsi tou dedomenoy trigwnou yparxei summetria ws pros y.
       Eksetazoune to trigwno sto thetiko tetartimorio kai xrisimopoiontas
       tin apoliti timi gia tis times tou x exoume kai tin periptwsi sto 
       2o tetartimorio. H pleura toy trigwnou einai 3*(1-x) otan x=0 y=3 kai
       gia x=1 y=0
    """
    result = -1
    if y>=0 and y <= -3*abs(x) + 3 :
        result = 1
    return result

def MC_double(f, g, x0, x1, y0, y1, n):
    """
    Monte Carlo oloklirwsi tis synartisis f se mia perioxi g>=0,
    poy perikleietai apo ena orthogwnio [x0,x1] * [y0,y1]. 
    n^2 einai o arithmos twn tyxaiwn simeiwn 
    """
    # Epilogi n**2 tyxaiwn simeiwn sto orthogwnio
    #x = np.random.uniform(x0, x1, n)
    #y = np.random.uniform(y0, y1, n)
    # Ypologismos tou athroismatos timwn tis f sti perioxi oloklirwsis
    f_mean = 0
    num_inside = 0            # plithos simeiwn x,y mesa stin perioxi (g>=0)
    for i in range(n):
        for j in range(n):
            x = x0+(x1-x0)*random()
            y = y0+(y1-y0)*random()
            if g(x, y) >= 0:
                num_inside += 1
                f_mean += f(x, y)
    f_mean = f_mean/num_inside
    area = (num_inside/n**2)*(x1 - x0)*(y1 - y0)
    return area*f_mean


seed(1234567)
Ntries = int(input("Posa deigmata na leifthoun? [Ntries = 1000] " ))
I_MC = MC_double(func,g,-1,1,0,3,Ntries)
I_exp = 0.5*(1-(-1))*(3-0)
print("The Area of the triangle is %4.3f " % I_MC)
print("The expected are is %4.0f" % I_exp)
