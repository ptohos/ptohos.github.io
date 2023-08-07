#!/usr/bin/python3
''' 
Usage (v1):
   chmod +x <filename>
   python3  <filename>

Usage (v2):
python3 
import <filename>

Description:
Introduction to string formatting

Notes:
The type can be used with format codes:
'd' for integers
'f' for floating-point numbers
'b' for binary numbers
'o' for octal numbers
'x' for octal hexadecimal numbers
'h' for hexadecimal numbers
's' for string
'e' for floating-point in an exponent format


Links:
https://docs.python.org/3/library/string.html
https://www.w3schools.com/python/ref_string_format.asp
'''
import numpy as np

msg = "=== 1) The value of pi is ~" + str(np.pi)
print(msg)

# empty {} interpreted as the next item in the format list
msg = "=== 2) The value of {} is ~ {:.5f}".format("pi", np.pi)
print(msg)


# explicit use of the format list item to use by the use of the list index
msg = "=== 3) The '{0}' of '{3}' is ~'{4:.5f}''".format("value", "not selected", "also not selected", "pi", np.pi)
print(msg)

msg = "=== 4) The '{1}' of '{2}' is ~'{4:.5f}'".format("value", "not selected", "also not selected", "pi", np.pi)
print(msg)

msg = "=== 5) '{0:d}' times '{1:d}' equals '{2:d}'".format(3, 2, 3*2)
print(msg)

msg = "=== 6) '{1:d}' times '{0:d}' equals '{2:d}'".format(3, 2, 3*2)
print(msg)

msg = "=== 7) for integer use {0:d}, for string use {1:s}', for binary use {2:b} or {3:b}, for exp use {4:e} ".format(3, "three", True, False, 100*100)
print(msg)

msg = "=== 8) %s has won the Nobel Prize %d times; in %s and %s.\n\tShe represents %.3f (%.2f %%) of 118 Nobel prizes in Physics awarded between 1901 and 2022." % ("Marie Curie", 2, "Phyics", "Chemistry", float(1/118), float(1/118)*(100.0) )
print(msg)

print("\n=== Quit!")
quit()
