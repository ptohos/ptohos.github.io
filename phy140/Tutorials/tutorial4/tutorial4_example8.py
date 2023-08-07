#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to functions

Links:
https://www.w3schools.com/python/python_operators.asp
https://www.tutorialspoint.com/python3/python_functions.htm
https://www.w3schools.com/python/trypython.asp?filename=demo_oper_mod

'''
def Print(msg, header=True):
    '''
    msg ....: string to be printed
    
    return..: nothing
    '''
    if (header):
        print("=== example5.py:\n\t", msg)
    else:
        print("\t", msg)
        
def isVowel(c):
    '''
    check if c, type string, is a vowel or not

    c : input character (string)

    return: true if vowel, false if consonant
    '''
    letter = c.lower()
    vowels = ["a", "e", "i", "o", "u"]
    
    # Return True if c is a vowel
    if letter in vowels:
        return True
    else:
        return False

def getVowelsFromPhrase(phrase):
    '''
     Takes a phrase, and returns a string of all the vowels

     Initalize an empty string to hold all of the vowels

    phase: string you want to loook for vowels in
    return list of vowels (string) found in phrase
    '''
    vowel_string = ''
    vowels = []
    for letter in phrase:
        # check if each letter is a vowel
        if isVowel(letter):
            vowels.append(letter)
        else:
            # if not a vowel, we don't care about it- so do nothing!
            pass #continue

    return vowels
    
## Testing
myPhrase = ""
try:
    msg = "Please type a phrase to look for vowels: "
    myPhrase = input(msg)
except:
    msg = "Something went wrong. Please type a phrase"
    Print(msg)

vList = getVowelsFromPhrase(myPhrase)
Print("Found %d vowels in the phrase '%s':" % (len(vList), myPhrase) )
for i,v in enumerate(vList, 1):
    Print("%d) %s" % (i, v), i==0)
quit()
