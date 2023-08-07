#!/usr/bin/python3

import random
from random import seed

NMCtries = int(input("How many MC tries? "))

seed(12345)
start_capital = 10
money = start_capital
for itry in range(NMCtries):
    money -= 1
    black = random.randint(1,6)
    white = random.randint(1,6)
    if black > white :
        money += 2

total_net_profit = money - start_capital
net_profit_per_game = total_net_profit/NMCtries
print("Net profit per game in the long run: ", net_profit_per_game)
if (net_profit_per_game<0):
    print("You should not play this game!!!")
else:
    print("It is a profitable game")
