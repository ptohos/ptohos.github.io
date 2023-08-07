#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to while loops

Links:

'''
i = 0
print("=== Simple example of while loop: ")
while i < 10:
    print("\ti = %d" % (i))
    i+=1
print("=== Outside of while loop. Quit!")


print("=== Another while-loop example: ")
j = 0
i = 0
while j < 1:
    if (i %2 == 0):
        print("\t%d is even number" % (i))
    else:
        print("\t%d is odd number" % (i))

    if i == 10:
        print("\ti = %d, j = %d. BREAK" % (i, j))
        break
    i+=1
quit()
