#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Examples of various Gaussian distributions

'''
import numpy as np
import matplotlib.pyplot as plt
import random as rndm

def getFWHM(sigma):
    return 2*sigma*np.sqrt(2*np.log(2))

def getGauss(x, mu, sigma):
    return (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*( (x-mu)/sigma)**2)

colours = ['b', 'r', 'g', 'c', 'm', 'y', 'k']

index = -1
for mean in [20, 60]:

    for sigma in [2, 5, 10]:
        index+= 1

        # Create the Gaussian function
        x = np.arange(0.0, 85.0, 1/100)
        y = [getGauss(v, mean, sigma) for v in x]

        # Enable the grid?
        plt.grid(True)
        
        # Draw the plot on the canvas
        plt.plot(x, y, colours[index], lw=3, label=r'$\mu=%.0f$, $\sigma=%.0f$' % (mean, sigma) )

        # Add information on canvas (labels, title)
        if index==0:
            plt.title("Guassian Distribution", size=12)
            plt.xlabel("x")
            plt.ylabel("probability density function (PDF)")

        # Add line at x=mean?
        plt.axvline(mean, color='k', linestyle="--", lw=1)
        
# Add legend to plot
plt.legend(title="Parameters: ")

plt.show()
quit()
