#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to using the print command (more detail than before)

Links:
https://python.land/introduction-to-python/functions
https://www.nobelprize.org/prizes/physics/1933/dirac/biographical/
'''
from myFunctions import *

say_hi("Paul Dirac", 3, 5, "PHYS-140")

# print(object(s), sep=separator, end=end, file=filename, flush=flush)
#print('Hello ', end='', flush=True)
#import time
#time.sleep(2)
#print('World!')

print("1) A physical law must possess mathematical beauty")
print("2) A physical law", "must possess", "mathematical beauty")
print("3) A physical law", "must possess", "mathematical beauty", sep=", ")
print("4) A physical law", "must possess", "mathematical beauty", sep="\t")
print("5) A physical law", "must possess", "mathematical beauty", sep=" ", end="!\n")
print("04", "10", "2022", sep="/", end="\n")


for i in range(10):
    print("%d) ", i, end="/9\n")



print("\n=== Quit!")
quit()
