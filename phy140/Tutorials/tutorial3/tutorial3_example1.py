#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to if/else concept

''' 
printIf = True
if (printIf):
    msg = "1) Hello world!"
else:
    msg = "1) Goodbye world!"
print(msg)


printIf = False
if (printIf):
    msg = "2) Hello world!"
else:
    msg = "2) Goodbye world!"
print(msg)
    

print("Quit!")
quit()

