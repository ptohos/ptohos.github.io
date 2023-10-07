# Lab 5 - Assignment 5


string = input("Give a string: ")
c1 = input("Give a character to search for: ")
c2 = input("Give the character to replace with: ")

str_len = len(string)
i = 0

while(i < str_len):
    if(string[i] == c1):
        print(c2, end='')
    else:
        print(string[i], end='')
    i = i + 1
