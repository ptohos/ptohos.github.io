#!/usr/bin/python3

def factorial(n):
    fact = 1
    num =  n
    if n < 0:
        print("Factorial of a negative integer is not defined")
        fact = 1
    while num >=1:
        fact = fact * num
        num = num - 1
    return fact

NSample = int(input("Poses dunates times arithmwn mporei na epileksei o diagonizomenos? "))
NChoice = int(input("Posous arithmous k mporei na epileksei o diagwnizomenos? "))

Npossible_choices = factorial(NSample)/(factorial(NChoice)*factorial(NSample-NChoice))
Probability = 1/Npossible_choices
print("H pithanotita na kerdisei to laxeio einai: ", Probability)

