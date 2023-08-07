#!/usr/bin/python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# the set-up
fig, ax = plt.subplots()
l = plt.plot([0],[0],'ko',markersize=20)
plt.xlabel('x'); plt.ylabel('y')
L = 2.2
ax = plt.axis([-L/2,L/2,-L/2,L/2])

pltorb, = plt.plot([], [], 'ko')

def animate(i): # here set up pltorb w/data, pass it to the animate
    x,y = np.cos(i),np.sin(i)
    pltorb.set_data(x,y) 
    return pltorb, 

nfrms = 90 # number of frames
frms = np.linspace(0,2*np.pi,nfrms) # each element corresponds to a frame

myanim = animation.FuncAnimation(fig, animate, frames=frms, \
       blit=True, repeat=True)
# in this funcion, animate(frms[i]) is called for i=0,1,...nfrms-1.

myanim.save('example_2.mp4', fps=30, extra_args=['-vcodec','libx264'])

plt.show()
