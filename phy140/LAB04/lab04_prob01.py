#!/usr/bin/python3

phrase = 'Einstein is a scientist'
count = 0
for letter in phrase:
    if letter == 'i':
        count+=1

print('The letter i appears ',count,' time in phrase ',phrase)
