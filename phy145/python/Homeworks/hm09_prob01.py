#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, randint


def Draw(BallsToDraw, MXBalls):
    selected_balls = []
    theball = randint(1,MXBalls)  # int random number sto [1,MXballs]
    selected_balls.append(theball)
    while len(selected_balls) < BallsToDraw:
        unique = True
        theball = randint(1,MXBalls)  # int random number sto [1,MXballs] 
        for pball in selected_balls:  # Check if ball has been drawn before
            if theball == pball:
                unique = False
                continue              # get out of the loop
        if unique:
            selected_balls.append(theball)
    selected_balls = np.array(selected_balls)
    SumOfBalls = sum(selected_balls)
    return SumOfBalls

def main():
    seed(123456)
    NBallsMx = 100    
    MxTries = int(input("Enter the number of experiments to perform "))
    NBalls = int(input("Enter the number of balls to draw "))
    mxscore = int(input("Enter the maximum score from the drawn balls: "))
    ok = NBalls >= 1 and NBalls <= NBallsMx
    if not ok:
        print("Invalid entry")
        print("Stop the execution")
        exit()
    else:
        success = 0
        for itries in range(MxTries):
            suma = Draw(NBalls, NBallsMx)
            if suma > mxscore:
                success +=1
        print(" The probability to get a score of %d out of %d balls is %5.2f"%
              (mxscore,NBalls,success*100/MxTries))

main()

        
