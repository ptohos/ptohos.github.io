#!/usr/bin/python3

from numpy.random import RandomState

alim = float(input("Please give the boundary of the walk "))

#Intatiate the RandomState
t = RandomState(123456)

print("No. of Walks \t  <Steps>")
for j in range(7):
    Ntries = 10**j                   # Number of experiments
    Sum    = 0                       # To athroisma twn vimatwn
    for itries in range(Ntries):     #----- This block of statements is a walk
        step = 0                     # number of steps for this walk
        Xpos = 0                     # initial position
        NmxStp =10000
        RNums  = t.rand(NmxStp)
        while abs(Xpos) <= alim:
            if t.rand() < 0.5:       # random number
                Xpos -= 1            # move to the left
            else:
                Xpos += 1            # move to the right
            step +=1                 # Moved by a step
        Sum += step                  # Add the number of steps for this walk to
 
                                     # the number of steps for all experiments
                                     #----- end of the block for a walk 
    AverageNumOfSteps = Sum/Ntries #
    print(' %10d \t %5.2f'%(Ntries,AverageNumOfSteps))
    
