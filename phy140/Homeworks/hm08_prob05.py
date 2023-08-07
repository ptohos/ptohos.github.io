#!/usr/bin/python3

from random import randint

def initialize(colors,numb_of_each_color):
    balls = []
    for k in range(len(colors)):
        for j in range(numb_of_each_color[k]):
            balls += [colors[k]]
    return balls

def draw(balls,number_of_balls_todraw):
    balls_drawn = []
    for ball in range(number_of_balls_todraw):
        index = randint(0,len(balls)-1)
        ball = balls.pop(index)
        balls_drawn.append(ball)
    return balls_drawn

def main():
    number_of_balls_todraw = 10
    Ntries = 500000
    all_colors    = ['red','blue','yellow','purple']
    numb_percolor = [10, 10, 10, 10]
    desired_color = ['red','blue']
    numb_wanted_of_each = [2, 2]

    Nsuccess = 0

    for itry in range(Ntries):
        balls = initialize(all_colors, numb_percolor)
        balls_drawn = draw(balls, number_of_balls_todraw)
        if balls_drawn.count(desired_color[0]) == numb_wanted_of_each[0] and \
           balls_drawn.count(desired_color[1]) == numb_wanted_of_each[1] :
            Nsuccess += 1
    print(70*'=')
    print('Probability to draw %1d %s balls and %1d %s balls in %d draws: %.6f'\
          %(numb_wanted_of_each[0], desired_color[0], \
            numb_wanted_of_each[1], desired_color[1], \
            number_of_balls_todraw, Nsuccess/Ntries))
    print(70*'=')

main()
