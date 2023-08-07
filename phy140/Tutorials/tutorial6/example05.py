#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
List comprehension

Links:
https://www.w3schools.com/python/python_lists_comprehension.asp
'''
from myFunctions import *

print("=== Filling a list with integers [0,10] with for-loop:")
numList = []
for i in range(11):
    numList.append(i)
print("\t%s" % (numList) )

print("\n=== Filling a list with integers [0,10] with list comprehension:")
numList = [i for i in range(11)]
print("\t%s" % (numList) )

print("\n=== Filling a list with all characters in a word with list comprehension:")
word  = "serendipity"
cList = [c for c in word]
print("\t%s" % (cList) )


print("\n=== Filling a list with manipulated integers [0,10] with list comprehension:")
powList = [powerN(i, 2) for i in range(11)]
print("\t%s" % (numList) )



print("\n=== Conditional list comprehension:")
evenList = [x for x in powList if x%2==0]
oddList  = [x for x in powList if x%2!=0]
altList  = [x for x in powList if x%2!=0 if x<20 if x>1]
print("\t %8s %10s" % ("evenList", evenList) )
print("\t %8s %10s" % ("oddList", oddList) )
print("\t %8s %10s" % ("altList", altList) )


print("\n=== More conditional list comprehension: if/else:")
myList = [str(x)+'=EVEN' if x%2==0 else str(x)+'=ODD' for x in range(1, 11, 1) ]
print("\t %8s %10s" % ("myList",  myList) )



print("\n=== More conditional list comprehension: nested for-loop:")
#nRows = 6
#nCols = 6
#idMatrix = [ [1 if c==r else 0 for r in range(nRows)] for c in range(nCols)]
idMatrix = getIdentityMatrix(6, 6)
#print("\tidMatrix",  idMatrix)
for row in idMatrix:
    print(row)



print("\n=== Quit!")
quit()

