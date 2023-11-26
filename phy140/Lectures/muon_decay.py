#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Original PDF
def pdf(costh, Pm):
    return [ 0.5 * (1.0 - 1.0/3.0 * Pm * x) for x in costh ]

# Positive solution of the inverse CDF
def inv_cdf_pos(r, P):
    return [3./P * (1.+np.sqrt(1. + 2./3. * P * (P/6. + 1. - 2.*x))) for x in r]

# Negative solution of the inverse CDF
def inv_cdf_neg(r, P):
    return [3./P * (1.-np.sqrt(1. + 2./3. * P * (P/6. + 1. - 2.*x))) for x in r]

def main():
    # Number of values we want to generate
    Ntries = 10000000
    # Generate random float numbers between [0,1] uniformly distributed
    r = np.random.uniform(0.0,1.0, size = Ntries)
    # We fix a value for P
    P=1.0

    data_pdf = inv_cdf_neg(r, P)  # The number of bins cannot be very large,
                                  # otherwise the histogram does not fit the
                                  # function.
    plt.hist(data_pdf, bins=100, density=True, histtype="step", color="black")

    x_axis = [-1.0+i*0.002 for i in range(1000)] 
    plt.plot(x_axis, pdf(x_axis, P) , color = "orange",linewidth = "1")
    
    plt.xlabel(r'$cos \ \theta$')
    plt.ylabel('f')
    plt.xlim(-1., 1.)
    plt.ylim(0.3, 0.7)
    plt.show()

main()
