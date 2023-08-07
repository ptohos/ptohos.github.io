#!/usr/bin/python3

import numpy as np

def guessingGame ():
    keepplaying = True
    while (keepplaying):
        for keys in Song:
            keys = input ("Which key would you like to guess?:\n")
            if keys in Song:
                a = input ("What is the " + keys + "?:\n")
                print(Song[keys], a)
                if Song[keys] == a:
                    print ("You are correct!!\n")
                else:
                    print ("You are WRONG!\n")
            else:
                print ("WRONG key!\n")
                yesno = input("Would you like to continue playing?:\n")
                if yesno.lower() == "no":
                    keepplaying = False
                    break

#========
# Main
#========
print("title:"+"\"We Are the Champions\"",
       "\nalbum:"+"\"News of the World\"",
       "\nartist:"+"\"Queen\"",
       "\ngenre:"+"\"Arena rock\"",
       "\nrelease year:",1977, 
       "\nlength:", 2.59,
       "\nlength (seconds):",179,
       "\nsongwriter:"+"\"Freddie Mercury\"",
       "\nproducers:"+"\"Queen, Mike \"Clay\" Stone")

print(30*("="),"\n Print as dictionary","\n"+30*("="))
# Dimiourgia tou Dictionary song me ta dedomena (attributes) tou tragoudiou 
Song = {
    "title": "We Are the Champions",
    "album": "News of the World",
    "artist": "Queen",
    "genre": "Arena rock",
    "release year": "1977",
    "length": "2.59",
    "length (seconds)": "179",
    "songwriter": "Freddie Mercury",
    "producers": "Queen, Mike \"Clay\" Stone"   # \" to \ xrisimopoieitai gia
}                                               # na typwthei to "


# Print tin pliroforia tou song se ena loop 
for key in Song:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), Song[key]))



def guess(key, val):
    return key in Song and Song[key] == val


print("\n\nBonus Game:\n\n")
print("Is the title of this song \"We Are the Champions\"?: {}".format(
    guess("title", "We Are the Champions")))
print("Is the album name \"News of the World\"?: {}".format(
    guess("album", "News of the World")))

r=0
print ("Here are the keys:")
for keys in Song:
    print(keys)

print("if you want to check press 1 if you want to guess press 2")
r=int(input())

keepgoing = True
if r == 1:
    while(keepgoing):
        for keys in Song:
            print("choose key:")
            keys=input()
            if keys in Song:
                print(Song[keys])
            else:
                keepgoing=False
                break
elif r == 2:
    guessingGame()
